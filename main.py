from data_cleaner import clean_srt_file

if __name__ == '__main__':
    clean_srt_file('data/22_hin.srt', 'data/cleaned/coda_hin.txt')
    clean_srt_file('data/Ratchasan (2018) WEBHD - CiniKingz.srt', 'data/cleaned/ratchasan_hin.txt')
    clean_srt_file('data/Pathaan.2023.WEBRip.AMZN.srt', 'data/cleaned/pathaan_hin.txt')
    clean_srt_file('data/Avengers.Endgame.2019.720p.WEB-DL.DD5.1.H264-CMRG-HI.hi.srt', 'data/cleaned/endgame_hin.txt')
    clean_srt_file('data/Servant.S03E08.Donut.720p.10bit.WEBRip.2CH.x265.HEVC-PSA.Hindi.HIN.srt', 'data/cleaned/servant_hin.txt')
