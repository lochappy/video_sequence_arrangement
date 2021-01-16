'''
Author: Loc Truong <ttanloc@gmail.com>
Date: 16Jan2021
Brief: This performs the unit test for the video-sequence arrangement algorithm
Usage:
    > python3 test_video_sequence_arrangement.py
'''
import unittest
from video_sequence_arrangement import foobar

class TestFoobar(unittest.TestCase):

    def test_empty_video_list(self):
        '''
        Test: 
            input          : empty video list and none-empty sequence
            expected output: empty list
        '''
        video_list = []
        sequence = [False, True, False, True, False, True, True, True, True, False ,False]
        exptected_output = []

        output = foobar(video_list, sequence)
        self.assertEqual(sorted(output), sorted(exptected_output))

    def test_empty_sequence(self):
        '''
        Test: 
            input          : empty sequence and none-empty video list
            expected output: empty list
        '''
        video_list = [('A',2),('B',2),('C',3)]
        sequence = []
        exptected_output = []

        output = foobar(video_list, sequence)
        self.assertEqual(sorted(output), sorted(exptected_output))

    def test_empty_video_and_sequence(self):
        '''
        Test: 
            input          : empty sequence and video list
            expected output: empty list
        '''
        video_list = []
        sequence = []
        exptected_output = []

        output = foobar(video_list, sequence)
        self.assertEqual(sorted(output), sorted(exptected_output))

    def test_video_longer_than_sequence(self):
        '''
        Test: 
            input          : single video list, the lenght of the video is longer than the sequence
            expected output: empty list
        '''
        video_list = [('A',8)]
        sequence = [False, True, False, True, False, True, False , False]

        exptected_output = []
        output = foobar(video_list, sequence)
        self.assertEqual(sorted(output), sorted(exptected_output))

    def test_total_length_of_videos_longer_than_sequence(self):
        '''
        Test: 
            input          : video list whose total length is longer than the sequence
            expected output: empty list
        '''
        video_list = [('A',3),('B',10)]
        sequence = [False, True, False, True, False, True, False , False]

        exptected_output = []
        output = foobar(video_list, sequence)
        self.assertEqual(sorted(output), sorted(exptected_output))

    def test_single_element_video_list(self):
        '''
        Test: 
            input          : single element video list and normal sequence
            expected output: eligible locations of the video in the sequence
        '''
        video_list = [('A',1)]
        sequence = [False, True, False, True, False, True, True, True, True, False , False]
        exptected_output = [[('A', 1)], [('A', 3)], [('A', 5)], [('A', 6)], [('A', 7)], [('A', 8)]]

        output = foobar(video_list, sequence)
        self.assertEqual(sorted(output), sorted(exptected_output))

    def test_3_elements_video_list(self):
        '''
        Test: 
            input          : 3 elements video list and normal sequence (similar to the one described in the task)
            expected output: eligible locations of the video in the sequence
        '''
        video_list = [('A',2),('B',2),('C',3)]
        sequence = [False, True, False, True, False, True, True, True, False ,False]

        exptected_output = [[('A', 1), ('B', 3), ('C', 5)],
                            [('A', 1), ('B', 3), ('C', 6)],
                            [('A', 1), ('B', 3), ('C', 7)],
                            [('A', 1), ('B', 5), ('C', 7)],
                            [('A', 3), ('B', 5), ('C', 7)],
                            ]

        output = foobar(video_list, sequence)
        self.assertEqual(sorted(output), sorted(exptected_output))

    def test_3_elements_video_list_v2(self):
        '''
        Test: 
            input          : 3 elements video list and normal sequence
            expected output: eligible locations of the video in the sequence
        '''
        video_list = [('A',3),('B',1),('C',2)]
        sequence = [True, True, False, False, True, False, True, True, False, False]

        exptected_output = [
                            [('A',0),('B',4),('C',6)],
                            [('A',0),('B',4),('C',7)],
                            [('A',0),('B',6),('C',7)],
                            [('A',1),('B',4),('C',6)],
                            [('A',1),('B',4),('C',7)],
                            [('A',1),('B',6),('C',7)]
                            ]

        output = foobar(video_list, sequence)
        self.assertEqual(sorted(output), sorted(exptected_output))

if __name__ == "__main__":
    unittest.main()