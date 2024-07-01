import os 
import shutil 
import tempfile 
import subprocess 

def delete_folder_contents(folder_path): 
    try: 
        for item in os.listdir(folder_path): item_path = os.path.join(folder_path, item) 
        
        if os.path.isfile(item_path) or os.path.islink(item_path): 
            os.unlink(item_path) 
        elif os.path.isdir(item_path): 
            shutil.rmtree(item_path) 
            print(f"Cleared contents of: {folder_path}")
    except Exception as e: 
        print(f"Failed to clear contents of {folder_path}. Reason: {e}") 
        
def clear_temp_files(): 
    temp_folder = tempfile.gettempdir() 
    delete_folder_contents(temp_folder) 
    
def empty_recycle_bin(): 
    try: 
        subprocess.run(['cmd', '/c', 'echo Y|PowerShell -NoProfile -Command Clear-RecycleBin'], shell=True, check=True) 
        print("Recycle Bin emptied.") 
    except subprocess.CalledProcessError as e: 
        print(f"Failed to empty Recycle Bin. Reason: {e}") 

def clear_browser_cache(): 
    browsers_cache_paths = { 
        'Chrome': os.path.expandvars(r'C:\Program Files\Google\Chrome\Application'), 
        'Firefox': os.path.expandvars(r'%APPDATA%\Mozilla\Firefox\Profiles'), 
        'Edge': os.path.expandvars(r'C:\Program Files (x86)\Microsoft\Edge\Application') } 
    
    for browser, path in browsers_cache_paths.items(): 
        
        if os.path.exists(path): 
            delete_folder_contents(path) 
            print(f"Cleared {browser} cache.") 
        else: print(f"{browser} cache path not found.") 
        
def get_user_confirmation(task_description): 
    
    while True: 
        user_input = input(f"Do you want to {task_description}? (yes/no): ").strip().lower() 
        if user_input in ['yes', 'no']: 
            return user_input == 'yes' 
        else: print("Invalid input. Please type 'yes' or 'no'.") 

def main(): 
    print("Starting C drive cleanup...") 

    if get_user_confirmation("clear temporary files"): 
        clear_temp_files() 
        
        if get_user_confirmation("empty the Recycle Bin"): empty_recycle_bin() 
        
        if get_user_confirmation("clear browser cache"): clear_browser_cache() 
        print("C drive cleanup completed.") 
        
if __name__ == "__main__": main()