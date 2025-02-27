import asyncio
import aiofiles
import argparse
import logging
from pathlib import Path


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)


async def copy_file(src_path: Path, dest_path: Path):
    """Asynchronously copies a file to the corresponding folder based on its extension."""
    try:
        async with aiofiles.open(src_path, "rb") as src, aiofiles.open(
            dest_path, "wb"
        ) as dest:
            await dest.write(await src.read())

        logging.info(f"Copied {src_path} to {dest_path}")

    except Exception as e:
        logging.error(f"Error copying {src_path} to {dest_path}: {e}")


async def read_folder(src_dir: Path, dest_dir: Path):
    """Recursively processes a folder, copying files based on their extensions to the corresponding subfolders."""
    tasks = []

    for item in src_dir.iterdir():
        if item.is_dir():
            tasks.append(read_folder(item, dest_dir))  # Process subdirectories
        elif item.is_file():
            file_ext = item.suffix[1:] if item.suffix else "no_extension"
            ext_dir = dest_dir / file_ext
            ext_dir.mkdir(
                parents=True, exist_ok=True
            )  # Create subfolder for the extension if it doesn't exist

            dest_path = ext_dir / item.name
            tasks.append(copy_file(item, dest_path))  # Add file copy task

    await asyncio.gather(*tasks)


async def main():
    """Main function that handles command-line arguments and starts the sorting process."""
    parser = argparse.ArgumentParser(
        description="Asynchronously copy and sort files by extension."
    )
    parser.add_argument("src_dir", type=str, help="Source directory")
    parser.add_argument(
        "dest_dir",
        type=str,
        nargs="?",
        default="dist",
        help="Destination directory (default: dist)",
    )

    args = parser.parse_args()

    src_dir = Path(args.src_dir).resolve()
    dest_dir = Path(args.dest_dir).resolve()

    if not src_dir.exists() or not src_dir.is_dir():
        logging.error(
            f"Source directory '{src_dir}' does not exist or is not a directory."
        )
        return

    dest_dir.mkdir(parents=True, exist_ok=True)

    await read_folder(src_dir, dest_dir)
    logging.info("File sorting completed.")


if __name__ == "__main__":
    asyncio.run(main())
