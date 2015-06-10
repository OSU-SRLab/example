from os import path
import sys

# This is a single-line comment. 

class InputFile:
    """ This class acts a container for input files. """
    
    filepath = ''
    filename = ''
    study = ''
    patient = ''
    sampleid = ''
    sample_type = ''
    capture_tech = ''
    date = ''
    miseq_id = ''
    bardcode_seq = ''
    lane = ''
    read = ''
    set_number = ''


    """ Initializer for class. """
    def __init__(self, filename=None):
        self.filename = filename
        if self.filename is not None:
            self.parse_filename()


    """ Parses the file's filename to extract parameters. """
    def parse_filename(self):
        if not self.filename or self.filename is None:
            print("InputFile error: Cannot parse an empty filename string!")
            return False


        """ 
        Split the filename into the appropriate path and filename sections.
        """
        split = self.filename.split('/')

        if len(split) is 1:
            """
            Only the filename (no path) was provided.
            """
            path  = ''
            filename = self.filename
        else:
            """
            Rejoin everything except the last part as the pathname;
            the last part should be the filename itself.
            """
            path = "/".join(split[0:-1])
            filename = split[-1]


        """ 
        Split the filename into pieces using the dash (-) character as
        a separator. Strip surrounding whitespace before splitting.
        """
        f = filename.strip().split('-')
        if len(f) is not 7:
            print("InputFile::parse_filename() error: "
                "Filename does not follow expected format.")
            return False

        self.filepath = path
        self.filename = filename
        self.study = f[0]
        self.patient = f[1]
        self.sampleid = f[2]
        self.sample_type = f[3]
        self.capture_tech = f[4]
        self.date = f[5]

        """
        Split the last MiSeq-appended string into appropriate params, using
        the underscore (_) as the separator.
        """
        m = f[6].split('_')
        self.miseq_id = m[0]
        self.bardcode_seq = m[1]
        self.lane = m[2][1:]
        self.read = m[3][1:]
        self.set_number = m[4]

