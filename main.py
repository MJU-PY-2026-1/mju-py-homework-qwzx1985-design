# 파일이름 :main.py
# 작 성 자 :박성현 60222032 환경시스템공학




account_balance =0.0
trade_history =[]

def display_menu():
    print('\n'+'='*35)
    print('비트코인 리스크 매니저 V3.0' )
    print('=*35')
    print('1.투자 자금 설정(입급)')
    print('2.선물 거래 시뮬레이션 시작')
    print('3.최종 자산 및 거래 내역 리포트')
    print('4.프로그랩 종료')
    print('='*35)

def initialize_balance(amount):
        global account_balance
        account_balance = float(amount)
        print(f'{account_balance:.2f}USDT 자산이 지갑에 충전되었습니다.')

def calculate_pnl(balance,rate,lev):
     pnl =(balance * (rate /100))*lev
     return pnl
    
def start_trading():
        global account_balance

        if account_balance <= 0:
            print('X 잔고가 부족합니다. 먼저 1번 메뉴에서 자금을 입금해주세요.')
            return
        
        print('\n[선물 거래 시뮬레이션]')
        leverage = int(input('레버리지를 설정하세요(1~125)'))
        change_rate = float(input('비트코인 예상 변동률(%)을 입력하세요:'))

        profit_loss = calculate_pnl(account_balance, change_rate, leverage )

        if change_rate > 0:
            status ='수익실현'
        elif change_rate <0:
            status = '손실발생'
            if abs(profit_loss) >= account_balance:
                print("[위험] 투자 원금이 전액 소실되어 '강제 청산'되었습니다!")
                account_balance = 0
                trade_history.append(f"강제 청산 발생 (손실: {profit_loss:.2f} USDT)")
                return
            
        else:
            status = '횡보장(변동없음)'

                
        account_balance += profit_loss
        trade_history.append(f'변동률{change_rate}% ({status})->결과:{profit_loss:.2f}USDT')
        print(f' 거래결과: {profit_loss:.2f}USDT ({status})')
        print(f' 현재잔고: {account_balance:.2f} USDT')

def show_report():
    print('\n'+"📊"*15)
    print("📊[실시간 자산 및 거래 기록 리포트]")
    print(f' 최종 보유 자산: {account_balance:.2f}USDT')
    print(f' 누적 거래 내역 : {trade_history}')
    print("📊"*15)

while True:
        display_menu()
        choice = input('원하는 메뉴 번호를 선택하세요:')

        if choice == '1':
            deposit_amount = input('입금할 금액(USDT)을 입력하세요: ')
            initialize_balance(deposit_amount)
        elif choice =='2':
            start_trading()
        elif choice == '3':
            show_report()
        elif choice =='4':
            print('\n프로그램을 안전하게 종료합니다. 이용해주셔서 감사합니다.')
            break
        else:
            print('X 올바르지 않는 번호입니다. 1번부터 4번 사이의 메뉴를 선택해주세요.')




