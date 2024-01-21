import os.path
import requests
import string
import random

headers = {
    "accept": "*/*",
    "accept-language": "he,en-US;q=0.9,en;q=0.8",
    "content-type": "application/json",
    "sec-ch-ua": r"\"Opera\";v=\"105\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": r"\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://www.opera.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

discord_url = 'https://api.discord.gx.games/v1/direct-fulfillment'


def gen(num_pos: int):
    parten_id = ''
    for i in range(36):
        num = random.choice(random.choice(string.digits + string.ascii_lowercase))
        parten_id = parten_id + num
        if len(parten_id) == 8:
            parten_id = parten_id + '-'
        elif len(parten_id) == 13:
            parten_id = parten_id + '-'
        elif len(parten_id) == 18:
            parten_id = parten_id + '-'
        elif len(parten_id) == 28:
            parten_id = parten_id + '-'
        elif len(parten_id) == 18:
            parten_id = parten_id + '-'
        elif len(parten_id) == 36:
            break
    jss = {"partnerUserId": parten_id}
    try:
        r = requests.post(json=jss, url=discord_url, headers=headers, timeout=100)
        r.raise_for_status()
        r = r.json()
        token = r['token']
        full_link = 'https://discord.com/billing/partner-promotions/1180231712274387115/' + token
        print(f'Code {num_pos} Successfuly generated.')
        return full_link
    except Exception as ass:
        print(f'Failed to generate {num_pos}, Trying Again.')
        gen(num_pos)


def main():
    while True:
        inp = input('Enter number of codes:\n')
        if inp == 'exit':
            break
        elif not inp.isdigit():
            print('Please type numbers only.')
            main()
        codes = []
        for i in range(int(inp)):
            codes.append(gen(i+1))

        if not os.path.exists('codes.txt'):
            file = open('codes.txt', 'w')
        else:
            file = open('codes.txt', 'a')
        for code in codes:
            file.write(f'{code}\n\n')

        file.close()
        break


if __name__ == '__main__':
    main()
