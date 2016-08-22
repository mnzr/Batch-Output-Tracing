from subprocess import call, Popen, PIPE
# call(["./spa", "args", "to", "spa"])


class Code:
    """Basic structure of code blocks"""
    count = 0
    def __init__(self, snippet):
        self.snippet = snippet
        Code.count += 1
        self.source = str(Code.count) + ".cpp"
        self.executive = str(Code.count) + ".out"
        self.output = str(Code.count) + ".txt"
        self.result = "ERROR: The code hasn't been run yet"

    def __str__(self):
        return str(self.count) + ": \n" + self.result

    def save(self):
        """saves the code to a file"""
        with open(self.source, 'w+') as saved:
            saved.write(self.snippet)

    def run(self):
        """runs the file"""
        self.save()

        # Gotta set stdout and stderr if you want to grab the output and err
        process = Popen(["g++", "-w", self.source, "-o", self.executive], stdout=PIPE, stderr=PIPE)
        _, error = process.communicate()

        if error != '': # This means the code didn't run perfectly
            self.result = "ERROR: " + error
            return
        else:
            # attempt to run the executive
            process = Popen(['./'+self.executive], stdout=PIPE, stderr=PIPE)
            self.result, err = process.communicate()
            try:
                # 'wb' means open in binary mode, plus writable. otherwise doesn't store any newline caracters.
                with open(self.output, 'wb') as out:
                    # print(result)
                    call(["rm", self.source, self.executive])
                    out.write(self.result)
            except Exception:
                self.result = "ERROR: Couldn't save the output!"
