from tkinter import *
from tkinter import ttk

from setuptools import Command
from pokeapi import get_pokemon_info

def main():
    #Create window
    root = Tk()
    root.title("Pokemon Info Viewer")
    root.iconbitmap('pokeicon.ico')
    root.resizable(False, False)

    #Create Frame  
    frm_input_top = ttk.Frame(root)
    frm_input_top.grid(row=1, column=1, columnspan=2)


    frm_stats_btmright = ttk.LabelFrame(root, text="Stats")
    frm_stats_btmright.grid(row=2, column=2, padx=10, pady=10, sticky=N)
    
    frm_info_btmleft = ttk.LabelFrame(root, text="Info")
    frm_info_btmleft.grid(row=2, column=1, padx=10, pady=10, sticky=N)

    #Populate user input frame
    lbl_name = ttk.Label(frm_input_top, text='Pokemon Name:')
    lbl_name.grid(row=0, column=0, padx=10, pady=10)

    entry_name = ttk.Entry(frm_input_top)
    entry_name.grid(row=0, column=1, padx=10, pady=10)

    def btn_get_info_click():
        name = entry_name.get()
        poke_dict = get_pokemon_info(name)
        if poke_dict: 
            lbl_height_val['text'] = str(poke_dict['height']) + ' dm'
            lbl_weight_val['text'] = str(poke_dict['weight']) + ' hg'
            types_list = (t['type']['name'] for t in poke_dict['types'])
            lbl_type_val['text'] = ', '.join(types_list)
            prg_hp['value'] = poke_dict['stats'][0]['base_stat']
            prg_attack['value'] = poke_dict['stats'][1]['base_stat']
            prg_defense['value'] = poke_dict['stats'][2]['base_stat']
            prg_spe_attack['value'] = poke_dict['stats'][3]['base_stat']
            prg_spe_defense['value'] = poke_dict['stats'][4]['base_stat']
            prg_speed['value'] = poke_dict['stats'][5]['base_stat']


    btn_get_info = ttk.Button(frm_input_top, text='Get Info', command = btn_get_info_click)
    btn_get_info.grid(row=0, column=2, padx=10, pady=10)

    #Populate stat fram
    lbl_hp = ttk.Label(frm_stats_btmright, text='HP:')
    lbl_hp.grid(row=0, column=0, padx= (10,0), pady=10, sticky=E)
    prg_hp = ttk.Progressbar(frm_stats_btmright, length=200, maximum=255.0)
    prg_hp.grid(row=0, column=1, padx= (0,10), pady=10)

    lbl_attack = ttk.Label(frm_stats_btmright, text='Attack:')
    lbl_attack.grid(row=1, column=0, padx= (10,0), sticky=E)
    prg_attack = ttk.Progressbar(frm_stats_btmright, length=200, maximum=255.0)
    prg_attack.grid(row=1, column=1, padx= (0,10), pady=10)

    lbl_defense = ttk.Label(frm_stats_btmright, text='Defense:')
    lbl_defense.grid(row=2, column=0, padx= (10,0), pady=10, sticky=E)
    prg_defense = ttk.Progressbar(frm_stats_btmright, length=200, maximum=255.0)
    prg_defense.grid(row=2, column=1, padx= (0,10), pady=10)
    
    lbl_spe_attack = ttk.Label(frm_stats_btmright, text='Special Attack:')
    lbl_spe_attack.grid(row=3, column=0, padx= (10,0), pady=10, sticky=E)
    prg_spe_attack = ttk.Progressbar(frm_stats_btmright, length=200, maximum=255.0)
    prg_spe_attack.grid(row=3, column=1, padx= (0,10), pady=10)

    lbl_spe_defense = ttk.Label(frm_stats_btmright, text='Special Defense:')
    lbl_spe_defense.grid(row=4, column=0, padx= (10,0), pady=10, sticky=E)
    prg_spe_defense = ttk.Progressbar(frm_stats_btmright, length=200, maximum=255.0)
    prg_spe_defense.grid(row=4, column=1, padx= (0,10), pady=10)

    lbl_speed = ttk.Label(frm_stats_btmright, text='Speed:')
    lbl_speed.grid(row=5, column=0, padx= (10,0), pady=10, sticky=E)
    prg_speed = ttk.Progressbar(frm_stats_btmright, length=200, maximum=255.0)
    prg_speed.grid(row=5, column=1, padx= (0,10), pady=10)

    #Populate info frame
    lbl_height = ttk.Label(frm_info_btmleft, text='Height:')
    lbl_height.grid(row=100, column=100, padx=10, pady=(10,0), sticky=E)
    lbl_height_val = ttk.Label(frm_info_btmleft, text='TBD', width=20)
    lbl_height_val.grid(row=100, column=200, padx=10, pady=(10,0), sticky=W)
     
    lbl_weight = ttk.Label(frm_info_btmleft, text='Weight:')
    lbl_weight.grid(row=200, column=100, padx=10, pady=(10,0), sticky=E)
    lbl_weight_val = ttk.Label(frm_info_btmleft, text='TBD')
    lbl_weight_val.grid(row=200, column=200, padx=10, pady=(10,0), sticky=W)

    lbl_type = ttk.Label(frm_info_btmleft, text='Type:')
    lbl_type.grid(row=300, column=100, padx=10, pady=(10,0), sticky=E)
    lbl_type_val = ttk.Label(frm_info_btmleft, text='TBD')
    lbl_type_val.grid(row=300, column=200, padx=10, pady=(10,0), sticky=W)








    
    root.mainloop()



    pass

main() 