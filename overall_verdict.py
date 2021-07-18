def overallVerdict(win_rate: int, avg_KD: float, avg_HS: int, matches: int, elo: int):
    overall = 0
    if 0 <= win_rate <= 65:
        overall = overall + 10
    else:
        overall = overall + 20
        
    if 0.0 <= avg_KD <= 1.5:
        overall = overall + 10
    else:
        overall = overall + 20

    if 0 <= avg_HS <= 65:
        overall = overall + 10
    else:
        overall = overall + 20

    if 0 <= matches <= 60 and elo > 2001:
        overall = overall + 40
    elif 0 <= matches <= 250 and elo > 1851:
        overall = overall + 35
    elif 0 <= matches <= 450 and elo > 1701:
        overall = overall + 30
    elif matches and elo > 0:
        overall = overall + 10
    elif 60 <= matches <= 115 and 1251 <= elo <= 1551:
        overall = overall + 15
    elif 0 <= matches <= 60 and 1251 <= elo <= 1551:
        overall = overall + 25
    elif 0 <= matches <= 60 and elo < 1251:
        overall = overall + 20
    elif 0 <= matches <= 300 and elo < 951:
        overall = overall + 10
    print(overall)
    verdict = ''
    if 85 <= overall <= 100:
        verdict = 'SMURF :clown: or CHEATER :skull_crossbones:'
    elif 70 <= overall <= 85:
        verdict = 'SMURF :clown:'
    elif overall < 70:
        verdict = 'LEGIT :white_check_mark: :100:'
    
    return overall, verdict