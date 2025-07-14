from pathlib import Path
from googletrans import Translator
import argparse
import os
import asyncio

def translate_subtitles(**kwargs):
	parser = argparse.ArgumentParser()
	parser.add_argument('--file', default='', help="full path of the subtitle file")
	parser.add_argument('--source_lang', default='ru', help="source language, default russian")
	parser.add_argument('--dest_lang', default='en', help="destination language, default english")
	args = parser.parse_args()
	
	new_file = set_new_filename(args.file, args.dest_lang)

	with open(args.file, "r") as source_file:
		with open(new_file, "w") as new_file:
			for line in source_file:
				translated  = asyncio.run(translate_line(line, args.dest_lang))
				new_file.write(translated+"\n")

def set_new_filename(file, dest_lang):
	file_path_parts = Path(file).parts
	filename, ext = os.path.splitext(file_path_parts[-1])

	return Path(*file_path_parts[:-1], filename + f".{dest_lang}{ext}")

async def translate_line(line, source_lang, dest_lang):
	async with Translator() as translator:
		line_lang = await translator.detect(line)
		should_translate = True if line_lang != dest_lang else False

		if should_translate:
			translated = await translator.translate(line, src=source_lang, dest=dest_lang)
			return str(translated.text)

		else:
			return line
