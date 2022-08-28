import requests, json
while True:
    try:
        api_method = input(
            '\033[92m[1]\033[0m: Show NFT contracts\n\033[92m[2]\033[0m: Show NFTs\n\033[92m[3]\033[0m: Create NFT contract\n\033[92m[4]\033[0m: Mint NFT\n\033[92m[5]\033[0m: Transfer NFT\n\033[92m[6]\033[0m: Show invoices\n\033[92m[7]\033[0m: Create invoice\n\033[92m[8]\033[0m: Cancel invoice\n\033[92m[9]\033[0m: Show wallets\n\033[92m[10]\033[0m: Create new wallet\n\n\033[1mSelect API method (1-10):\033[0m '
        )

        try:
            api_key
        except:
            api_key = input(
                '\033[94mAPI key\033[0m \033[93m(skip for new key)\033[0m:\n')
            if not api_key:
                api_key = requests.get('https://thentic.tech/api/key').text
                print('\033[94mYour API key\033[0m: ' + api_key)
        try:
            chain_id
        except:
            chain_id = input(
                '\033[94mEVM chain id\033[0m \033[93m(skip for 97 - Binance testnet)\033[0m:\n'
            )
            if not chain_id:
                chain_id = '97'

        if api_method == '1':
            print('Getting NFT contracts..')

            url = 'https://thentic.tech/api/contracts'
            headers = {'Content-Type': 'application/json'}
            data = {'key': api_key, 'chain_id': chain_id}

            r = requests.get(url, json=data, headers=headers)
            try:
                if len(json.loads(r.text)['contracts']) == 0:
                    print('No contracts created yet')

                for i in json.loads(r.text)['contracts']:
                    try:
                        print('\033[92m' + i['name'] + ' (' + i['short_name'] +
                              ')\033[0m:\n  \033[94mstatus\033[0m: ' +
                              i['status'] + '\n  \033[94mrequest id\033[0m: ' +
                              i['request_id'] +
                              '\n  \033[94mcontract\033[0m: ' + i['contract'])
                    except:
                        print('\033[92m' + i['name'] + ' (' + i['short_name'] +
                              ')\033[0m:\n  \033[94mstatus\033[0m: ' +
                              i['status'] + '\n  \033[94mrequest id\033[0m: ' +
                              i['request_id'] +
                              '\n  \033[94mtransaction url\033[0m: ' +
                              i['transaction_url'] +
                              '\n  \033[94mtransaction pixel\033[0m: ' +
                              i['transaction_pixel'])

            except:
                print('\033[93m' + 'Please try again' + '\033[0m')

            if r.text == 'API key not authorized. Get key: https://thentic.tech/api/key':
                print(r.text)
                api_key = input(
                    '\033[94mAPI key\033[0m \033[93m(skip for new key)\033[0m:\n'
                )
                if not api_key:
                    api_key = requests.get('https://thentic.tech/api/key').text
                    print('\033[94mYour API key\033[0m: ' + api_key)
            elif r.text == 'Chain not found':
                print(r.text)
                chain_id = input(
                    '\033[94mEVM chain id\033[0m \033[93m(skip for 97 - Binance testnet)\033[0m:\n'
                )
                if not chain_id:
                    chain_id = '97'
            else:
                input('\033[93mPress any key to continue\033[0m\n')
        elif api_method == '2':
            print('Getting NFTs..')

            url = 'https://thentic.tech/api/nfts'
            headers = {'Content-Type': 'application/json'}
            data = {'key': api_key, 'chain_id': chain_id}

            r = requests.get(url, json=data, headers=headers)
            try:
                if len(json.loads(r.text)['nfts']) == 0:
                    print('No NFTs created yet')

                for i in json.loads(r.text)['nfts']:

                    print('\033[92m' + i['name'] + ' (' + i['short_name'] +
                          ')\033[0m:\n  \033[94mstatus\033[0m: ' +
                          i['status'] + '\n  \033[94mrequest id\033[0m: ' +
                          i['request_id'] + '\n  \033[94mcontract\033[0m: ' +
                          i['contract'] + '\n  \033[94mid\033[0m: ' + i['id'] +
                          '\n  \033[94mdata\033[0m: ' + i['data'] +
                          '\n  \033[94mtransaction url\033[0m: ' +
                          i['transaction_url'] +
                          '\n  \033[94mtransaction pixel\033[0m: ' +
                          i['transaction_pixel'])

            except:
                print('\033[93m' + 'Please try again' + '\033[0m')

            if r.text == 'API key not authorized. Get key: https://thentic.tech/api/key':
                print(r.text)
                api_key = input(
                    '\033[94mAPI key\033[0m \033[93m(skip for new key)\033[0m:\n'
                )
                if not api_key:
                    api_key = requests.get('https://thentic.tech/api/key').text
                    print('\033[94mYour API key\033[0m: ' + api_key)
            elif r.text == 'Chain not found':
                print(r.text)
                chain_id = input(
                    '\033[94mEVM chain id\033[0m \033[93m(skip for 97 - Binance testnet)\033[0m:\n'
                )
                if not chain_id:
                    chain_id = '97'
            else:
                input('\033[93mPress any key to continue\033[0m\n')

        elif api_method == '3':

            name = input('\033[94mNFT Name:\033[0m\n')
            short_name = input('\033[94mNFT Symbol:\033[0m\n')

            print('Creating NFT contract..')

            url = 'https://thentic.tech/api/nfts/contract'
            headers = {'Content-Type': 'application/json'}
            data = {
                'key': api_key,
                'chain_id': chain_id,
                'name': name,
                'short_name': short_name
            }

            r = requests.post(url, json=data, headers=headers)

            try:
                print(
                    '\033[92m' + name + ' (' + short_name + ')' +
                    '\033[0m\n  \033[94mstatus\033[0m: pending\n  \033[94mrequest id\033[0m: '
                    + json.loads(r.text)['request_id'] +
                    '\n  \033[94mtransaction url\033[0m: ' +
                    json.loads(r.text)['transaction_url'])
            except:
                print('\033[93m' + 'Please try again' + '\033[0m')
            if r.text == 'API key not authorized. Get key: https://thentic.tech/api/key':
                print(r.text)
                api_key = input(
                    '\033[94mAPI key\033[0m \033[93m(skip for new key)\033[0m:\n'
                )
                if not api_key:
                    api_key = requests.get('https://thentic.tech/api/key').text
                    print('\033[94mYour API key\033[0m: ' + api_key)
            elif r.text == 'Chain not found':
                print(r.text)
                chain_id = input(
                    '\033[94mEVM chain id\033[0m \033[93m(skip for 97 - Binance testnet)\033[0m:\n'
                )
                if not chain_id:
                    chain_id = '97'
            else:
                input('\033[93mPress any key to continue\033[0m\n')
        elif api_method == '4':
            nft_contract = input(
                '\033[94mNFT Contract address (0x..):\033[0m\n')
            nft_id = input('\033[94mNFT On-chain ID:\033[0m\n')
            nft_data = input('\033[94mEncrypted data:\033[0m\n')
            nft_to = input('\033[94mOwner address (0x..):\033[0m\n')

            print('Minting NFT..')

            url = 'https://thentic.tech/api/nfts/mint'
            headers = {'Content-Type': 'application/json'}
            data = {
                'key': api_key,
                'chain_id': chain_id,
                'contract': nft_contract,
                'nft_id': nft_id,
                'nft_data': nft_data,
                'to': nft_to
            }

            r = requests.post(url, json=data, headers=headers)

            try:
                print(
                    '  \033[94mstatus\033[0m: pending\n  \033[94mrequest id\033[0m: '
                    + json.loads(r.text)['request_id'] +
                    '\n  \033[94mtransaction url\033[0m: ' +
                    json.loads(r.text)['transaction_url'])
            except:
                print('\033[93m' + 'Please try again' + '\033[0m')
            if r.text == 'API key not authorized. Get key: https://thentic.tech/api/key':
                print(r.text)
                api_key = input(
                    '\033[94mAPI key\033[0m \033[93m(skip for new key)\033[0m:\n'
                )
                if not api_key:
                    api_key = requests.get('https://thentic.tech/api/key').text
                    print('\033[94mYour API key\033[0m: ' + api_key)
            elif r.text == 'Chain not found':
                print(r.text)
                chain_id = input(
                    '\033[94mEVM chain id\033[0m \033[93m(skip for 97 - Binance testnet)\033[0m:\n'
                )
                if not chain_id:
                    chain_id = '97'
            else:
                input('\033[93mPress any key to continue\033[0m\n')

        elif api_method == '5':
            nft_contract = input(
                '\033[94mNFT Contract address (0x..):\033[0m\n')
            nft_id = input('\033[94mNFT On-chain ID:\033[0m\n')
            nft_from = input('\033[94mTransfer from address (0x..):\033[0m\n')
            nft_to = input('\033[94mTransfer to address (0x..):\033[0m\n')

            print('Transferring NFT..')

            url = 'https://thentic.tech/api/nfts/transfer'
            headers = {'Content-Type': 'application/json'}
            data = {
                'key': api_key,
                'chain_id': chain_id,
                'contract': nft_contract,
                'nft_id': nft_id,
                'from': nft_from,
                'to': nft_to
            }

            r = requests.post(url, json=data, headers=headers)

            try:
                print(
                    '  \033[94mstatus\033[0m: pending\n  \033[94mrequest id\033[0m: '
                    + json.loads(r.text)['request_id'] +
                    '\n  \033[94mtransaction url\033[0m: ' +
                    json.loads(r.text)['transaction_url'])
            except:
                print('\033[93m' + 'Please try again' + '\033[0m')
            if r.text == 'API key not authorized. Get key: https://thentic.tech/api/key':
                print(r.text)
                api_key = input(
                    '\033[94mAPI key\033[0m \033[93m(skip for new key)\033[0m:\n'
                )
                if not api_key:
                    api_key = requests.get('https://thentic.tech/api/key').text
                    print('\033[94mYour API key\033[0m: ' + api_key)
            elif r.text == 'Chain not found':
                print(r.text)
                chain_id = input(
                    '\033[94mEVM chain id\033[0m \033[93m(skip for 97 - Binance testnet)\033[0m:\n'
                )
                if not chain_id:
                    chain_id = '97'
            else:
                input('\033[93mPress any key to continue\033[0m\n')

        elif api_method == '6':
            print('Getting invoices..')

            url = 'https://thentic.tech/api/invoices/all'
            headers = {'Content-Type': 'application/json'}
            data = {'key': api_key, 'chain_id': chain_id}

            r = requests.get(url, json=data, headers=headers)
            try:
                if len(json.loads(r.text)['invoices']) == 0:
                    print('No invoices created yet')

                for i in json.loads(r.text)['invoices']:
                    print('\033[92m' + i['amount'] + ' ' + i['currency'] +
                          '\033[0m:\n  \033[94mstatus\033[0m: ' + i['status'] +
                          '\n  \033[94mrequest id\033[0m: ' + i['request_id'] +
                          '\n  \033[94mtransaction url\033[0m: ' +
                          i['transaction_url'])

            except:
                print('\033[93m' + 'Please try again' + '\033[0m')

            if r.text == 'API key not authorized. Get key: https://thentic.tech/api/key':
                print(r.text)
                api_key = input(
                    '\033[94mAPI key\033[0m \033[93m(skip for new key)\033[0m:\n'
                )
                if not api_key:
                    api_key = requests.get('https://thentic.tech/api/key').text
                    print('\033[94mYour API key\033[0m: ' + api_key)
            elif r.text == 'Chain not found':
                print(r.text)
                chain_id = input(
                    '\033[94mEVM chain id\033[0m \033[93m(skip for 97 - Binance testnet)\033[0m:\n'
                )
                if not chain_id:
                    chain_id = '97'
            else:
                input('\033[93mPress any key to continue\033[0m\n')

        elif api_method == '7':
            invoice_amount = input('\033[94mInvoice Amount:\033[0m\n')
            invoice_to = input('\033[94mReceiver address (0x..):\033[0m\n')

            print('Generating Invoice..')

            url = 'https://thentic.tech/api/invoices/new'
            headers = {'Content-Type': 'application/json'}
            data = {
                'key': api_key,
                'chain_id': chain_id,
                'amount': invoice_amount,
                'to': invoice_to
            }

            r = requests.post(url, json=data, headers=headers)

            try:
                print(
                    '  \033[94mstatus\033[0m: pending\n  \033[94mrequest id\033[0m: '
                    + json.loads(r.text)['request_id'] +
                    '\n  \033[94mtransaction url\033[0m: ' +
                    json.loads(r.text)['transaction_url'])
            except:
                print('\033[93m' + 'Please try again' + '\033[0m')

            if r.text == 'API key not authorized. Get key: https://thentic.tech/api/key':
                print(r.text)
                api_key = input(
                    '\033[94mAPI key\033[0m \033[93m(skip for new key)\033[0m:\n'
                )
                if not api_key:
                    api_key = requests.get('https://thentic.tech/api/key').text
                    print('\033[94mYour API key\033[0m: ' + api_key)
            elif r.text == 'Chain not found':
                print(r.text)
                chain_id = input(
                    '\033[94mEVM chain id\033[0m \033[93m(skip for 97 - Binance testnet)\033[0m:\n'
                )
                if not chain_id:
                    chain_id = '97'
            else:
                input('\033[93mPress any key to continue\033[0m\n')

        elif api_method == '8':
            request_id = input('\033[94mInvoice Request ID:\033[0m\n')

            print('Cancelling Invoice..')

            url = 'https://thentic.tech/api/invoices/cancel'
            headers = {'Content-Type': 'application/json'}
            data = {
                'key': api_key,
                'chain_id': chain_id,
                'request_id': request_id
            }

            r = requests.delete(url, json=data, headers=headers)

            print(r.text)
            if r.text == 'API key not authorized. Get key: https://thentic.tech/api/key':
                #print(r.text)
                api_key = input(
                    '\033[94mAPI key\033[0m \033[93m(skip for new key)\033[0m:\n'
                )
                if not api_key:
                    api_key = requests.get('https://thentic.tech/api/key').text
                    print('\033[94mYour API key\033[0m: ' + api_key)
            elif r.text == 'Chain not found':
                print(r.text)
                chain_id = input(
                    '\033[94mEVM chain id\033[0m \033[93m(skip for 97 - Binance testnet)\033[0m:\n'
                )
                if not chain_id:
                    chain_id = '97'
            else:
                input('\033[93mPress any key to continue\033[0m\n')
        elif api_method == '9':
            print('Getting wallets..')

            url = 'https://thentic.tech/api/wallets/all'
            headers = {'Content-Type': 'application/json'}
            data = {'key': api_key, 'chain_id': chain_id}

            r = requests.get(url, json=data, headers=headers)

            try:
                if len(json.loads(r.text)['wallets']) == 0:
                    print('No wallets created yet')

                for i in json.loads(r.text)['wallets']:
                    print('\033[94m' + i + '\033[0m')
            except:
                print('\033[93m' + 'Please try again' + '\033[0m')

            if r.text == 'API key not authorized. Get key: https://thentic.tech/api/key':
                print(r.text)
                api_key = input(
                    '\033[94mAPI key\033[0m \033[93m(skip for new key)\033[0m:\n'
                )
                if not api_key:
                    api_key = requests.get('https://thentic.tech/api/key').text
                    print('\033[94mYour API key\033[0m: ' + api_key)
            elif r.text == 'Chain not found':
                print(r.text)
                chain_id = input(
                    '\033[94mEVM chain id\033[0m \033[93m(skip for 97 - Binance testnet)\033[0m:\n'
                )
                if not chain_id:
                    chain_id = '97'
            else:
                input('\033[93mPress any key to continue\033[0m\n')
        elif api_method == '10':
            print('Creating new wallet..')

            url = 'https://thentic.tech/api/wallets/new'
            headers = {'Content-Type': 'application/json'}
            data = {'key': api_key}

            r = requests.post(url, json=data, headers=headers)

            try:
                print('\033[94m  wallet\033[0m: ' +
                      json.loads(r.text)['wallet'] +
                      '\n  \033[94mprivate key\033[0m: ' +
                      json.loads(r.text)['private_key'] +
                      '\n\033[91mDO NOT SHARE PRIVATE KEY WITH ANYONE\033[0m')
            except:
                print('\033[93m' + 'Please try again' + '\033[0m')

            if r.text == 'API key not authorized. Get key: https://thentic.tech/api/key':
                print(r.text)
                api_key = input(
                    '\033[94mAPI key\033[0m \033[93m(skip for new key)\033[0m:\n'
                )
                if not api_key:
                    api_key = requests.get('https://thentic.tech/api/key').text
                    print('\033[94mYour API key\033[0m: ' + api_key)
            elif r.text == 'Chain not found':
                print(r.text)
                chain_id = input(
                    '\033[94mEVM chain id\033[0m \033[93m(skip for 97 - Binance testnet)\033[0m:\n'
                )
                if not chain_id:
                    chain_id = '97'
            else:
                input('\033[93mPress any key to continue\033[0m\n')
        else:
            print('\033[93m' + 'Please try again' + '\033[0m')
    except:
        print('\033[93m' + 'Please try again' + '\033[0m')
