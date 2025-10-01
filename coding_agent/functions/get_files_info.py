import os

def get_files_info(working_directory, directory=None):
   abs_working_directory = os.path.abspath(working_directory)
   if directory is None:
       directory = "."
   abs_directory = os.path.join(directory)  
   if not abs_directory.startswith(abs_working_directory):
       raise ValueError("The directory must be within the working directory.")


   final_response = ""
   contents = os.listdir(abs_directory)    
   for content in contents:
      content_path = os.path.join(abs_directory, content)
      is_dir = os.path.isdir(content_path)
      size = os.path.getsize(content_path)
      
        