'''
Author: Loc Truong <ttanloc@gmail.com>
Date: 19Jan2021
Brief: This is the video-sequence arrangement algorithm
Usage:
    > python3 video_sequence_arrangement_loop.py -v Path/to/video/file -s Path/to/sequence/file
'''

from argparse import ArgumentParser
import itertools

def foobar(video_list, sequence, start_index=0, list_of_selected_videos=[]):
    '''
    This function arranges the list of videos to the sequence.
    @param: 
            input:  video_list: list of videos, in the form of [(Name0,length0), (Name1,length1)...]
                    sequence: list of sequence of scenes, in form of [True, False, True...]
                    start_index: start index location of the current sequence.
                    list_of_selected_videos: list of the videos included in the previous iteration

            output: return the list of possible locations of the video list in the sequence
    '''

    # if total length of the video is greater than the sequence, return []
    total_length = 0
    for video in video_list:
        total_length += video[1]
    if total_length > len(sequence):
        return []

    # check empty video list or sequence
    if len(video_list) == 0 or len(sequence) == 0:
        return []

    def check_location(location, video_list, sequence):
        '''
        This function validate if the given location is the right fit for the video list in the sequence
        @param: 
                input:  location: location of interest.
                        video_list: list of the video
                        sequence: sequence of scenes
                output: True if the location is valid
                        False if the location is invalid
        '''
        # check if all the location are valid
        true_loc = True
        for loca in location:
            true_loc = true_loc and sequence[loca]
        if not true_loc:
            return False

        # check if the last video lasts longer than the sequence
        if (location[-1] + video_list[-1][1] > len(sequence)):
            return False

        # check if there is any overlapping between the 2 consecutive video
        for idx in range(len(location) - 1):
            if (location[idx] + video_list[idx][1]) > location[idx+1]:
                return False
        
        return True

     # create all of the possible locations.
    sequence_index = [list(range(len(sequence))) for _ in range(len(video_list))]
    possible_location_index = itertools.product(*sequence_index)
    
    # looking for the valid locations
    possible_postions_of_videos = []
    for loca in possible_location_index:
        if check_location(loca, video_list, sequence):
            arrangement = [(video[0],start_idx) for video, start_idx in zip(video_list,loca)]
            possible_postions_of_videos.append(arrangement)

    return possible_postions_of_videos

if __name__ == "__main__":

    # parse the argument
    parser = ArgumentParser(description='Arrange video list to the sequence')
    parser.add_argument('-v', metavar='Path/to/text/file', type=str, required=True, dest='video_list',
                        help='Path to text file containing list of video')
    parser.add_argument('-s', metavar='Path/to/text/file', type=str, required=True, dest='sequence',
                        help='Path to text file containing sequence of scene')

    args = parser.parse_args()

    # read the sequence file
    with open(args.sequence,'r') as f:
        sequence = [line == 'T' for line in f.read().splitlines()]

    # read the video list
    with open(args.video_list,'r') as f:
        video_list = [line.split(',') for line in f.read().splitlines()][1:]
    video_list = [ (video[0], int(video[1])) for video in video_list]

    # compute the possible location of the video list
    possible_locations = foobar(video_list, sequence)

    # print out the result.
    if possible_locations:
        print('\n###### Possible arrangement #######\n')
        for pos in possible_locations:
            print(pos)
        print('\n##################################\n')
    else:
        print('\n##################################')
        print('## No possible arrangement found #')
        print('##################################\n')
