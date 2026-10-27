import sqlite3
import struct
import zlib
from config import DATABASE_PATH, read_statements

(text_vs_bytes, hex_and_codes, create_table, insert_file,
 read_info, png_checks, total_bytes, read_content) = read_statements(__file__)


def make_png(width, height, red, green, blue):
    """Build a tiny, real PNG picture as bytes. No picture library is needed."""

    def chunk(kind, data):
        body = kind + data
        return struct.pack(">I", len(data)) + body + struct.pack(">I", zlib.crc32(body))

    one_row = b"\x00" + bytes([red, green, blue]) * width      # filter byte + the pixels
    pixels = one_row * height
    return (
        b"\x89PNG\r\n\x1a\n"                                                    # the PNG signature
        + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))  # picture header
        + chunk(b"IDAT", zlib.compress(pixels, 0))                               # the pixels
        + chunk(b"IEND", b"")                                                    # the end marker
    )


connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def show(title, statement, params=()):
    print(title)
    print("-" * len(title))
    cursor.execute(statement, params)
    for row in cursor.fetchall():
        print(row)


show("TEXT counts characters, bytes are counted by BLOB", text_vs_bytes)
print()
show("HEX, UNICODE, CHAR and ZEROBLOB", hex_and_codes)

cursor.execute(create_table)
png_bytes = make_png(4, 4, 255, 0, 0)               # a 4 x 4 red picture
cursor.execute(insert_file, ("greeting.txt", "text", "Hello from SQLite"))
cursor.execute(insert_file, ("tiny_red.png", "image", png_bytes))
connection.commit()
print("\nTwo files stored: a text file and a picture")

print()
show("What was stored (the picture is a BLOB)", read_info)
print()
show("Is it really a PNG? The first 8 bytes say so", png_checks)
print()
show("Storage used by the two files", total_bytes)

cursor.execute(read_content, ("tiny_red.png",))
stored = cursor.fetchone()[0]
width, height = struct.unpack(">II", stored[16:24])

print("\nReading the picture back into Python")
print("------------------------------------")
print("Python gets it back as                  :", type(stored).__name__)
print("Identical to the picture we stored      :", stored == png_bytes)
print(f"Width x height read from the file header: {width} x {height}")

connection.close()