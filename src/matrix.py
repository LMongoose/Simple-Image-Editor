# Native Modules
import os, subprocess
# Downloaded Modules

# Custom Modules



class Matrix(object):
    def __init__(self, p_matrix):
        self.matrix = p_matrix
        self.height = len(self.matrix)
        self.width = len(self.matrix[0])

    @staticmethod
    def read_from(p_filepath):
        _pngfilepath = p_filepath
        _pgmfilepath = os.path.splitext(p_filepath)[0] + ".pgm"
        try:
            subprocess.call("imagemagick\\convert {0} -colorspace gray -compress none -depth 8 {1}".format(_pngfilepath, _pgmfilepath))
        except:
            raise Exception("File {0} could not be opened.".format(p_filepath))
        else:
            del _pngfilepath
            try:
                with open(_pgmfilepath) as pgmfile:
                    _text = pgmfile.readlines()[3:-1]
                _matrix = []
                for line in _text:
                    _matrix.append(line[0:-2].split(" "))
                del _text
            except:
                raise Exception("File {0} could not be opened.".format(p_filepath))
            else:
                os.remove(_pgmfilepath)
                del _pgmfilepath
                return Matrix(_matrix)

    def write_to(self, p_filepath):
        """
        Saves the Matrix Object as a new png file.
        """
        try:
            _pgmfilepath = "temp.pgm"
            with open(_pgmfilepath, "w+") as pgmfile:
                pgmfile.write("P2\n")
                pgmfile.write("{0} {1}\n".format(self.width, self.height))
                pgmfile.write("255\n")
                for row in self.matrix:
                    for item in row:
                        pgmfile.write(item+" ")
                    pgmfile.write("\n")
            subprocess.call("imagemagick\\convert {0} {1}".format(_pgmfilepath, p_filepath))
        except:
            raise Exception("Error saving file {0}.".format(p_filepath))
        finally:
            os.remove(_pgmfilepath)
            del _pgmfilepath

    def option1(self):
        _newmatrix = []
        for row in self.matrix[0:-1:2]:
            _newline = row[0:-1:2]
            _newmatrix.append(_newline)
        return Matrix(_newmatrix)

    def option2(self):
        _newmatrix = []
        for row in self.matrix:
            _row = []
            for char in row:
                if((int(char) % 2) == 0):
                    _row.append(char)
            _newmatrix.append(_row)
        return Matrix(_newmatrix)

    def option3(self):
        _newmatrix = []
        for row in self.matrix[1:-1:2]:
            _newline = row[1:-1:2]
            _newmatrix.append(_newline)
        _newmatrix2 =[]
        for row in _newmatrix:
            _row = []
            for char in row:
                if((int(char) % 2) == 0):
                    _row.append(char)
            _newmatrix2.append(_row)
        return Matrix(_newmatrix2)

    def option4(self):
        _newmatrix = []
        for row in self.matrix:
            _row = []
            for cell in row:
                _newvalue = int(cell) + 10
                if(_newvalue > 255):
                    _row.append(str(255))
                else:
                    _row.append(str(_newvalue))
            _newmatrix.append(_row)
        return Matrix(_newmatrix)

    def option5(self):
        _newmatrix = []
        for row in self.matrix:
            _row = []
            for cell in row:
                _newvalue = int(cell) - 10
                if(_newvalue < 0):
                    _row.append(str(0))
                else:
                    _row.append(str(_newvalue))
            _newmatrix.append(_row)
        return Matrix(_newmatrix)

    def option6(self):
        _newmatrix = []
        for row in self.matrix:
            _row = []
            for cell in row:
                _row.append(str(255-int(cell)))
            _newmatrix.append(_row)

        return Matrix(_newmatrix)
