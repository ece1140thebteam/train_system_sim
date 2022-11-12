import unittest
import Track
import TrackBlock
import track_model_gui

class TestTrackModelClass(unittest.TestCase):
    def test_parse_file(self):
        track = track_model_gui.parse_track('blueline.csv')
        for line in track.track_lines:
            assert('Blue' in line)
            for block in track.track_lines[line].blocks:
                assert(block>=1 and block<=15)

    def test_add_block(self):
        track = track_model_gui.parse_track('blueline.csv')
        b = TrackBlock.TrackBlock(
            line = "Test",
            section = "Test",
            block_number = "404",
            block_len = "404",
            block_grade = "404",
            speed_limit = "404",
            underground = "Test",
            station = "Test",
            switch = "Test",
            elevation = "404",
            has_rail_crossing = "Test",
            cum_elevation = "404",
            can_travel_to = "Test"
        )
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
        assert(track.track_lines['Test'].blocks[404].switch         == "Test")
        assert(track.track_lines['Test'].blocks[404].can_travel_to  == "Test")
        assert(track.track_lines['Test'].blocks[404].has_rail_crossing == "Test")


    def test_set_maintenance_mode(self):
        pass


if __name__ == '__main__':
    unittest.main()