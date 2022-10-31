from strategy import *


class PositionManager:
    orders = [None] * 3
    
    def __init__(self,symbol):
        self.symbol = symbol
    
    
    
    # 포지션 3개 한번에 설정
    # mode : buy or sell
    def set_position(self,binance,position_size):
        self.binance = binance
        self.position_size = position_size
        
        # market sell
        # 시장가 진입
        self.orders[0] = self.binance.create_order(
            symbol=self.symbol,
            type="MARKET",
            side="sell",
            amount=self.position_size
        )

        # take profit 
        # 목표가는 전략에 따라 다름
        # 우선은 퍼센트로 구현함
        
        self.orders[1] = self.binance.create_order(
            symbol=self.symbol,
            type="TAKE_PROFIT_MARKET",
            side="buy",
            amount=self.position_size,
            params={'stopPrice': 20800}
        )

        # stop loss
        # 목표가는 전략에 따라 다름
        
        self.orders[2] = self.binance.create_order(
            symbol=self.symbol,
            type="STOP_MARKET",
            side="buy",
            amount=self.position_size,
            params={'stopPrice': 20600}
        )

    
    # 거래 내역 저장
    def save_log(self):
        pass
    
    
    def __del__(self):
        pass