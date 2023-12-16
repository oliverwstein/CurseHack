import re

def convert_monster_definition(c_text):
    python_monsters = {}

    # Regex pattern to identify each monster entry
    pattern = r'MON\("(.*?)",\s*(.*?),\s*LVL\(([^,]+,[^,]+,[^,]+,[^,]+,[^,]+)\),\s*\((.*?)\),\s*A\((.*?)\),\s*SIZ\((.*?)\),\s*([^,]+),\s*([^,]+),\s*(.*?)\),'


    matches = re.finditer(pattern, c_text, re.DOTALL)
    for match in matches:
        name, symbol, level, gen_flags, attacks, size, *rest = match.groups()
        
        # Process the level and gen_flags
        try:
          level = level.replace('\n', '').replace(' ', '').split(',')
        except:
          print(name, symbol, level)
        gen_flags = tuple(gen_flags.replace('\n', '').replace(' ', '').split('|'))

        # Process the attacks
        attack_list = []
        for atk in re.findall(r'ATTK\((.*?)\)', attacks):
            attack_list.append(tuple(atk.replace('\n', '').replace(' ', '').split(',')))

        # Process the size
        size = tuple(size.replace('\n', '').replace(' ', '').split(','))
        resists = rest[0].replace('\n', '').replace(' ', '').split('|')
        resists_conveyed = rest[1].replace('\n', '').replace(' ', '').split('|')
        flags = rest[-1].replace('\n', '').replace(' ', '').split(',')[0:3]
        m1 = flags[0].split('|')
        m2 = flags[1].split('|')
        m3 = flags[2].split('|')
        color = rest[-1].replace('\n', '').replace(' ', '').split(',')[-1]

        # Add the parsed monster to the dictionary
        python_monsters[name.lower().replace(' ', '_')] = {
            "name": name,
            "symbol": symbol,
            "level": level,
            "gen_flags": gen_flags,
            "attacks": attack_list,
            "size": size,
            "resists": resists,
            "resists_conveyed": resists_conveyed,
            "flags1": m1,
            "flags2": m2,
            "flags3": m3,
            "color": color.strip()
        }

    return python_monsters