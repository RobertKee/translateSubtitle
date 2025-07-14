import unittest
import subtitle_translate

class TestStringMethods(unittest.TestCase):

    def test_file_name_setter(self):
        filename = "/Users/robert/Plex Media/Movies/Kura-no.naka(1981)Yoichi.Takabayashi/Kura-no.naka(1981)Yoichi.Takabayashi.srt"
        new_file = subtitle_translate.set_new_filename(filename, 'en')

        self.assertEqual("/Users/robert/Plex Media/Movies/Kura-no.naka(1981)Yoichi.Takabayashi/Kura-no.naka(1981)Yoichi.Takabayashi.en.srt"
, str(new_file))
