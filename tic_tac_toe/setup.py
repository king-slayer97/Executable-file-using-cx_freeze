from cx_Freeze import setup, Executable
 
setup(name = "tic_tac_toe" ,
      version = "0.1" ,
      description = "Some stuff" ,
      executables = [Executable("tic_tac_toe.py")])
