import os , shutil, json

def create_dir(path : str, name : str ):
    mk_directory = os.path.join(path, name)
    try:
        os.makedirs( mk_directory )
    except:
        print(f"Directory already exists {mk_directory}")


def remove_dir( path : str, name: str):
    rm_directory = os.path.join(path, name)
    try: 
        shutil.rmtree( rm_directory )
    except:
        print(f"Directory not found {rm_directory} ")


def save_to_file(data, tournament_id, tournament_round)-> None:
    with open(f'./{tournament_id}/round_{tournament_round}.json', 'w') as fp:     
        json.dump(data, fp, indent=3) 
    
def load_round(tournament_id, round_numb):
    r_directory = os.path.join(f"{tournament_id}", f"round_{round_numb}.json")
    try: 
        with open(r_directory, 'r')as file :
            return json.load(file) 
    except FileNotFoundError: 
        print("File not found")