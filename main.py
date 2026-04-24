# 파일이름 :main.py
# 작 성 자 :박성현 60222032 환경시스템공학

print('=== 비트코인 수익률 5일 시뮬레이터 V2.0 ===')

balance = float(input('초기 투자 원금을 입력하세요 (USDT): '))
leverage = int(input('레버리지를 설정하세요 (1~123):'))
daily_history = []

for day in range(1,6):
    print(f'\n{day}일차 거래 프로세스')
    change_rate = float(input(f'{day}일차 비트코인 예상 변동률(%)을 입력하세요'))


    profit_loss = (balance * (change_rate / 100)) * leverage

    if change_rate > 0:
        statue = '수익 실현'
    elif change_rate < 0:
        status = '손실 발생'

        if abs(profit_loss) >= balance:
            print("[위험]투자 원금이 전액 소실되어 '강제청산'되었습니다!")
            balance = 0
            daily_history.append(f'{day}일차 : 강제 청산 (거래종료)')
            break   
else:
    status = '횡보장 (변동 없음)'
    balance =+ profit_loss
    daily_history.append(f'{day}일차: {profit_loss:.2f}USDT({status})')

print('\n'+'='*45)
print('[실시간 투자 수익률 리포트]')
print(f'최종 자산 현활: {balance:.2f} USDT')
print(f'전체 거래 내역: {daily_history}')
print('='* 45)
print('시뮬레이션이 모두 완료되었습니다. 수고하셨습니다.')

