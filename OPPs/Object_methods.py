class student:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name    

    ## Public Method
    def name(self):
        print(self.f_name, self.l_name)

    # Private Info
    def __info(self):
        print("This is confidential")

