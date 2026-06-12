# 파일이름 :main.py
# 작 성 자 :박성현 60222032 환경시스템공학




account_balance =0.0
trade_history_2d =[]

def display_menu():
    print('\n'+'='*35)
    print('비트코인 리스크 매니저 V4.0(최종판)' )
    print('='*35)
    print('1.투자 자금 설정(입금)')
    print('2.선물 거래 시뮬레이션 시작')
    print('3.최종 자산 및 거래 내역 리포트')
    print('4.프로그램 종료')
    print('='*35)

def load_data():
    global account_balance, trade_history_2d
    try:
        with open('bitcoin_report.txt','r',encoding='utf-8') as f:
            lines = f.readlines()
            if lines:
                print('\n[안내] 이전 저장된 데이터를 성공적으로 불러왔습니다.')
    except FileNotFoundError:
        print('\n[안내] 기존에 저장된 성적/거래 파일이 없습니다. 새로 시작합니다')

def start_trading():
    global account_balance, trade_history_2d

    if account_balance <= 0:
        print('잔고가 부족합니다. 먼저 1번 메뉴에서 자금을 입금해주세요.')
        return
    
    print('\n[선물 거래 시뮬레이션]')
    try:
        coin_name = input('거래할 코인 이름(예: BTC,ETH)을 입력하세요: ')
        leverage = int(input('레버리지를 설정하세요(1~125): '))
        change_rate = float(input('예상 변동률(%)을 입력하세요: '))
    except ValueError:
        print('[오류] 레버리지와 변동률은 반드시 숫자로 입력해야 합니다! 거래 취소.')
        return
    
    profit_loss = (account_balance * (change_rate/100)) * leverage

    if change_rate > 0:
        status = '수익실현'
    elif change_rate < 0:
        status = '손실발생'
        if abs(profit_loss) >= account_balance:
            print("[위험] 투자 원금이 전액 소실되어 '강제 청산'되었습니다!")
            account_balance = 0
            trade_history_2d.append([coin_name, leverage, change_rate, profit_loss, '강제 청산'])
            return
        
    else:
        status = '횡보장(변동없음)'

    account_balance += profit_loss
    trade_history_2d.append([coin_name, leverage, change_rate, profit_loss, status ])

    print(f'거래결과: {profit_loss:.2f} USDT ({status})')
    print(f'현재잔고: {account_balance:.2f} USDT')

def show_and_save_report():
    print('\n' + '📊'* 15)
    print('📊[실시간 자산 및 거래 기록 리포트]')
    print(f'최종 보유 자산: {account_balance:.2f} USDT')
    print ('-'* 40)
    print('코인명 | 레버리지 | 변동률 | 손익결과 | 상태')
    print('-'*40)
    
    for record in trade_history_2d:
        print(f'{record[0]} | {record[1]}x | {record[2]}% | {record[3]:.2f} USDT, | {record[4]} ')
    
    print('📊'* 15)

    try:
        with open('bitcoin_report.txt', 'w', encoding='utf-8') as f:
            f.write(f'최종 자산: {account_balance:.2f} USDT\n')
            f.write('코인명,레버리지,변동률,손익,상태\n')
            for record in trade_history_2d:
                f.write(f'{record[0]},{record[1]},{record[2]},{record[3]:.2f},USDT{record[4]}\n')
        print("\n✅ 거래 내역이 'bitcoin_report.txt' 파일로 안전하게 저장되었습니다!")
    except Exception as e:
        print(f'파일 저장 중 오류가 발생했습니다: {e}')

load_data()

while True:
    display_menu()
    choice = input('원하는 메뉴 번호를 선택하세요: ')

    if choice == '1':
        try:
            deposit_amount = float(input('입금할 금액 (USDT)을 입력 하세요: '))
            account_balance += deposit_amount
            print(f'{account_balance:.2f} USDT 자산이 지갑에 충전 되었습니다')
        except ValueError:
            print('🚨 [오류] 입금액은 숫자로만 입력해주세요!')

    elif choice == '2' :
        start_trading()

    elif choice == '3' : 
        show_and_save_report()
    
    elif choice == '4' :
        print('\n프로그램을 안전하게 종료합니다. 이용해주셔서 감사합니다.')
        break

    else:
        print('🚨 올바르지 않은 번호입니다. 1번부터 4번 사이의 메뉴를 선택해주세요.')
                



