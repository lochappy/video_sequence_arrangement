'''
Author: Loc Truong <ttanloc@gmail.com>
Date: 16Jan2021
Brief: This is the video-sequence arrangement algorithm
Usage:
    > python3 video_sequence_arrangement.py -v Path/to/video/file -s Path/to/sequence/file
'''

from argparse import ArgumentParser

def foobar(video_list, sequence, start_index=0, list_of_prev_videos=[]):
    '''
    This function arranges the list of video to the sequence.
    @param: 
            input:  video_list: list of video, in the form of [(Name0,length0), (Name1,length1)...]
                    sequence: list of sequence of scenes, in form of [True, False, True...]
                    start_index: start index location of the current sequence.
                    list_of_prev_videos: list of the videos included in the previous iteration

            output: return the list of possible locations of the video list in the sequence
    '''
    # if total length of the video is greater than the sequence, return []
    total_length = 0
    for video in video_list:
        total_length += video[1]
    if total_length > len(sequence):
        return []

    # base case: empty video list or sequence
    if len(video_list) == 0 or len(sequence) == 0:
        return []

    curr_video_name, curr_video_len = video_list[0]

    # base case: there is only one video in the list
    if len(video_list) == 1:
        possible_postions_of_last_video = []
        for index in range(start_index,len(sequence)):
            if sequence[index] and (index + curr_video_len) <=len(sequence):
                possible_postions_of_last_video.append(list_of_prev_videos + [(curr_video_name, index)])
        return possible_postions_of_last_video
    
    # Normal case: there are more than one video in the list
    possible_postions_of_videos = []
    for index in range(start_index,len(sequence)):
        if sequence[index] and (index + curr_video_len)<=len(sequence):
            new_possible_locations = foobar(video_list[1:], sequence, index + curr_video_len, list_of_prev_videos + [(curr_video_name, index)])
            possible_postions_of_videos = possible_postions_of_videos + new_possible_locations
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
