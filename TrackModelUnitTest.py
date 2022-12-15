import unittest
from track_model.track_model_qc import Track
from track_model.track_model_qc import TrackBlock
from track_model.track_model_qc.widget import TrackModel
from PyQt6.QtWidgets import QApplication, QWidget, QTreeWidgetItem, QFileDialog
from signals import s

import sys

class TestTrackModelClass(unittest.TestCase):
    def test_parse_file(self):
        app = QApplication(sys.argv)
        tm = TrackModel()
        for line in tm.track.track_lines:
            assert('Green' in line or 'Red' in line)
            for block in tm.track.track_lines[line].blocks:
                assert(block>=0)

    def test_add_block(self):
        app = QApplication(sys.argv)
        tm = TrackModel()        
        b = TrackBlock.TrackBlock(
            line = "Test",
            section = "Test",
            block_number = "404",
            block_len = "404",
            block_grade = "404",
            speed_limit = "404",
            underground = "Test",
            station = "Test",
            switch = None,
            elevation = "404",
            has_rail_crossing = "Test",
            cum_elevation = "404",
            can_travel_to = "Test"
        )
        track = tm.track
        track.add_block(b)
        
        assert('Test' in track.track_lines)
        assert(404 in track.track_lines['Test'].blocks)
        assert(track.track_lines['Test'].blocks[404].block_len      == 404)
        assert(track.track_lines['Test'].blocks[404].block_grade    == 404)
        assert(track.track_lines['Test'].blocks[404].speed_limit    == 404)
        assert(track.track_lines['Test'].blocks[404].cum_elevation  == 404)
        assert(track.track_lines['Test'].blocks[404].block_number   == 404)
        assert(track.track_lines['Test'].blocks[404].underground    == "Test")
        assert(track.track_lines['Test'].blocks[404].station        == "Test")
        assert(track.track_lines['Test'].blocks[404].switch         == None)
        assert(track.track_lines['Test'].blocks[404].can_travel_to  == "Test")
        assert(track.track_lines['Test'].blocks[404].has_rail_crossing == "Test")


if __name__ == '__main__':
    unittest.main()