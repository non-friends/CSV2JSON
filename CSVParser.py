#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Bryan .
@Bryan .

Made with love by Bryan .

==================================
DESC:
    Will return the parsed CSV file given as
a python dict or JSON. This is meant to be
read and has functions that you may use in
other projects.
==================================

VERSION: 1.0.0.1

"""


def parseCSV(csvDoc,
         output_type="dict",
         start_parse=0,
         row_parse_offset=1):
    from re import compile as c
    from numpy import array
    from json import dumps
    """
    A Simple function to parse csv files.

    Just chuck in the raw text of the csv (clean or dirty) and this parser
    will throw an output (Specified or unspecified. default:JSON).

    Args:
        csvDoc (any): The document to parse
        output_type (str): The output type
        start_parse (int): The starting row when parsing
        row_parse_offset (int): The offset of the row when parsing
    Returns:
        dict: A dictionary

    Raises:
        None

    """

    csvparser = c(
        '(?:(?<=,)|^)\\s*\\"?((?<=\\")[^\\"]*(?=")|[^,\\"]*?)\\"?\\s*(?=,|$)')
    # csvparser = c('(?<!,\"\\w)\\s*,(?!\\w\\s*\",)')
    lines = str(csvDoc).split('\n')[start_parse:]
    # lines = lines[start_parse:]

    # All the lines are not empty
    necessary_lines = [line for line in lines if line != ""]

    # We might need to add a redundant comma stripper

    All  = array([csvparser.findall(line)
                 for line in necessary_lines])
    def doDict(All):
        # All the python dict keys required (At the top of the file or top row)
        main_table = {}      # The parsed data will be here
        top_line   = list(All[0])
        for name in All[1:]: # The top line
            name      = name[row_parse_offset:]  # Getting the actual name
            right_now = name[0]
            main_table[right_now] = {}

            for thing in top_line[1:]:
                try:
                    proc_name = name[top_line.index(thing)]
                except IndexError:
                    proc_name = ''
                finally:
                    main_table[right_now][thing] = proc_name
        # print('Returning parsed stuff')

        return dumps(main_table, skipkeys=True, ensure_ascii=False, indent=1)

    if output_type.lower() in {"dict", "json"}:  # If you want JSON or dict
        returnme = doDict(All)
        return returnme
    elif output_type.lower() in {
        "list", "numpy", "array", "matrix",
        "np.array", "np.ndarray","numpy.array",
        "numpy.ndarray"}:
        return list(All)
    else:
        returnme = doDict(All)
        return returnme


def ComplexParseCSV(csvDoc,
             output_type="json",
             start_parse=0,
             start_parse_column=0,
             delimeter=',',
             line_delimiter='\n',
             row_parse_offset=1,
             top_line_column_offset=1):
    """A more advanced version of parseCSV

    Parameters
    ----------
    csvDoc : type
        The CSV document to parse.
    output_type : type
        The type of the output you want.
    The following are still WIP.
    start_parse : type
        Description of parameter `start_parse`.
    start_parse_column : type
        Description of parameter `start_parse_column`.
    delimeter : type
        Description of parameter `delimeter`.
    ' : type
        Description of parameter `'`.
    line_delimiter : type
        Description of parameter `line_delimiter`.
    row_parse_offset : type
        Description of parameter `row_parse_offset`.
    top_line_column_offset : type
        Description of parameter `top_line_column_offset`.

    Returns
    -------
    Varies
        It varies between a python dict, JSON, or a numpy array.

    """
    from re import compile as c
    from numpy import array
    from json import dumps

    csvparser = c(
        f'(?:(?<={str(delimeter)})|^)\\s*\\"?((?<=\\")[^\\"]*(?=")|[^{str(delimeter)}\\"]*?)\\"?\\s*(?={str(delimeter)}|$)'
        )
    # csvparser = c('(?<!,\"\\w)\\s*,(?!\\w\\s*\",)')
    lines = str(csvDoc).split(str(line_delimiter))[start_parse:]
    # lines = lines[start_parse:]

    # All the lines are not empty
    necessary_lines = [line for line in lines if line != ""]

    # We might need to add a redundant comma stripper

    All  = array([csvparser.findall(line)
                 for line in necessary_lines])
    def doDict(All):
        # All the python dict keys required (At the top of the file or top row)
        main_table = {}      # The parsed data will be here
        top_line   = list(All[0])
        # top_left_corner = top_line[0]
        # top_right_corner = top_line[len(top_line)]
        # bottom_line = All[len(All)]
        # bottom_left_corner = bottom_line[0]
        # bottom_right_corner = bottom_line[len(bottom_line)]
        for name in All[row_parse_offset:]:
            name = name[start_parse_column:]
            right_now = name[0]
            main_table[right_now] = {}

            for thing in top_line[start_parse_column +
                                  top_line_column_offset:]:
                try:
                    proc_name = name[top_line.index(thing)]
                except IndexError:
                    proc_name = ''
                finally:
                    main_table[right_now][thing] = proc_name
        # print('Returning parsed stuff')

        return dumps(main_table, skipkeys=True, ensure_ascii=False, indent=1)

    if output_type.lower() in {"dict", "json"}:  # If you want JSON or dict
        returnme = doDict(All)
        return returnme
    elif output_type.lower() in {
        "list", "numpy", "array", "matrix",
        "np.array", "np.ndarray","numpy.array",
        "numpy.ndarray"}:
        return list(All)
    else:
        returnme = doDict(All)
        return returnme


class CSVparser(object): # For parsing csv files
    def __init__(self,
                 filecontents,                    # Contents of the file
                 line_delimiter=r"\n",
                 rows_start_anchor=0,             # Starting row
                 rows_end_anchor=None,            # Ending row
                 top_line_column_start_anchor=1,  # Starting top line column
                 top_line_column_end_anchor=None, # Ending top line column
                 main_row_column_start_anchor=0,  # Starting main row column
                 main_row_column_end_anchor=None,
                 main_top_line_index_offset=1):# Ending main row column
        # Note: Should we parse these later? Or do we do them like this?
        # We're doing it like this for now.
        """The __init__ script.

        Parameters
        ----------
        filecontents : str (or an object that has a str method)
            The contents of the csv file.
        ARGUMENTS:
            TBD.

        Returns
        -------
        None
            Bruh, it's nothing!

        """
        self.csv = filecontents
        csvDoc = str(filecontents)
        from re import compile as c
        from numpy import array
        from json import dumps
        ldemiter = c(line_delimiter)
        lines = ldemiter.split(str(csvDoc))
        necessary_lines = [line for line in lines if line != ""]

        if rows_end_anchor != None:

            necessary_lines = necessary_lines[  # To cut to the margins of
                # rows_start_anchor and rows_end_anchor
                rows_start_anchor:rows_end_anchor]
        else:
            necessary_lines = necessary_lines[rows_start_anchor:]  # Or just
            # rows_start_anchor if rows_end_anchor is None

        csvparser = c(
            '(?:(?<=,)|^)\\s*\\"?((?<=\\")[^\\"]*(?=")|[^,\\"]*?)\\"?\\s*(?=,|$)')
        All  = array([csvparser.findall(line)
                    for line in necessary_lines])
        self.list = All
        # All the python dict keys required (At the top of the file or top row)
        main_table = {}      # The parsed data will be here
        top_line   = list(All[0])
        # top_line processing
        if top_line_column_end_anchor != None:
            top_line = top_line[
                top_line_column_start_anchor:top_line_column_end_anchor]
        else:
            top_line = top_line[top_line_column_start_anchor:]  # Or just
            # rows_start_anchor if rows_end_anchor is None


        for name in All[1:]:
            # var name processing
            if main_row_column_end_anchor != None:
                name = name[
                    main_row_column_start_anchor:main_row_column_end_anchor]
            else:
                name = name[main_row_column_start_anchor:]  # Or just
                # main_row_column_start_anchor if rows_end_anchor is None
            right_now = name[0]
            main_table[right_now] = {}
            for thing in top_line:
                try:
                    proc_name = name[top_line.index(thing) +
                                     main_top_line_index_offset]
                except IndexError:
                    proc_name = ''
                finally:
                    main_table[right_now][thing] = proc_name
        self.json = dumps(main_table, skipkeys=True, ensure_ascii=False,
                                 indent=1)

    def as_json(self):
        """
        Returns the JSON representation.
        JSON = python dict
        """
        return self.json

    def as_dict(self):
        """
        A alias for as_json
        """
        return self.as_json()

    def as_list(self):
        """
        Returns the list representation.
        Python list/array
        """
        return list(self.list)

    def as_table(self):
        """
        A alias for as_list
        """
        return self.as_list()

    def as_array(self):
        """
        A alias for as_list
        """
        return self.as_list()

    def as_csv(self):
        return self.csv
