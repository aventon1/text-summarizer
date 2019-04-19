#!/usr/bin/env python3

"""TODO: put a description of this file"""

# TODO: Put author names here

from data_input import get_data
from content_selection import select_content
from info_ordering import order_info
from content_realization import realize_content
#from evaluation import eval_summary
from sys import argv
import os


def write_summary_files(summaries):
    """
    This function takes in a dict {topic: [(sentence)]}
    generated by realize_content(summaries_in_order)
    in text_summarizer.py main.
    It should output a file for each topic with the final summary.
    """
	
	# Testing # TODO: remove when done
	summary_files = []
	
    # Directory where output files should be
    output_dir = "../outputs/D2/"

    # TODO: change unique file numbering system if needed
    numeric_count = 1

    for topic_id in summaries:
        # Split topic ID into 2 parts
        id_part1 = topic_id[:-1]
        id_part2 = topic_id[-1:]

        # Make output file name and directory
        file_path = output_dir + "{}-A.M.100.{}.{}".format(id_part1, id_part2, str(numeric_count))
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
			
		# add file to array
    	summary_files.append(file_path)
    
        with open(file_path, "w") as out_file:

            # write sentences to topic output file
            for sentences in summaries[topic_id]:
                out_file.write(sentences + "\n")

        #TODO: change to a counter if writing multiple files for one topic in one run
        #numeric_count += 1
	
	# Testing # TODO: remove when done
	print(summary_files)

if __name__ == '__main__':

	# TODO: modify this to accept command line arguments
	# which will have a configuration file for which data to read in
	# that is then passed into get_data

	# TODO: Make this work with condor as an input arg
#	input_list = argv[1]
	input_list = ['/dropbox/18-19/573/Data/Documents/training/2009/UpdateSumm09_test_topics.xml',
            '/dropbox/18-19/573/Data/Documents/devtest/GuidedSumm10_test_topics.xml']

	# Read in input data
	# and return a list of Topic objects (with documents/sentences)
	topics = get_data(input_list)


	# Content Selection
	# identifies salient sentences & ranks them
	# & chooses up to 100 words (using full sentences)
	# returns a dictionary of {topic_id: [(sentence, date)]}
	topic_summaries = select_content(topics)


	# Information Ordering
	# orders sentences by date for each topic
	# returns a dictionary of {topic_id: [sentences]}
	summaries_in_order = order_info(topic_summaries)

	# Content Realization
	# process sentences to make well-formed
	# return a 2D array of well-formed sentences in order for each topic
	summaries = realize_content(summaries_in_order)

	# Write summary to file for each topic
	# No return. Files written to directory '../outputs/D2/'
	write_summary_files(summaries)


	# Evaluate summaries for each topic
	# Run ROUGE-1 & ROUGE-2 on the summary
	# TODO: modify this file to get ROUGE passed in
	# (or should it be hard-coded?)
#	eval_summary()




