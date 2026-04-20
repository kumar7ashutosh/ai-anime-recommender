import pandas as pd

class DataLoader:
    def __init__(self,old_file:str,new_file:str):
        self.old_file=old_file
        self.new_file=new_file
        
    def load_and_process(self):
        df_old=pd.read_csv(self.old_file,encoding='utf-8').dropna()
        df_old.rename(columns={'sypnopsis':'synopsis'},inplace=True)
        req_cols={'Name','Genres','synopsis'}
        print(df_old.columns)
        res=req_cols-set(df_old.columns)
        if res:
            raise ValueError("missing columns in csv files")
        
        df_old['combined_info']=("Title: "+df_old['Name']+" ,Overview: "+df_old['synopsis']+" ,Genre: "+df_old['Genres']+" ,Rating: "+df_old['Score'].astype(str)+"/10")
        df_old[['combined_info']].to_csv(self.new_file,index=False,encoding="utf-8")
        
        return self.new_file
        