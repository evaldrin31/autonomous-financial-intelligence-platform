# Paper Trading Engine: Autonomous Financial Intelligence Platform

## Executive Summary

The Paper Trading Engine provides a risk-free simulation environment where users can test investment strategies, validate AI agent decisions, and build confidence before deploying real capital. This module is critical for both user safety and AI training.

---

## 1. Paper Trading Overview

### 1.1 Purpose

| Objective | Description |
|-----------|-------------|
| Risk-Free Testing | Test strategies without real money |
| AI Validation | Validate autonomous decisions |
| Strategy Development | Refine approaches before live trading |
| Education | Learn trading without consequences |
| Backtesting | Test on historical data |

### 1.2 Simulation Fidelity

The paper trading engine aims for high fidelity:
- **Price Accuracy**: Real-time or historical market data
- **Slippage Modeling**: Realistic execution prices
- **Commission Simulation**: Actual broker fees
- **Market Impact**: Large order effects
- **Timing**: Accurate execution timestamps

---

## 2. Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                  PAPER TRADING ENGINE                       │
└─────────────────────────────────────────────────────────────┘

┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   Market     │───>│   Simulator  │───>│   Results    │
│   Data       │    │   Engine     │    │   Store      │
└──────────────┘    └──────┬───────┘    └──────────────┘
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
    ┌────▼────┐      ┌────▼────┐      ┌─────▼─────┐
    │  Price  │      │  Order  │      │ Portfolio │
    │  Feed   │      │  Match  │      │ Tracker   │
    └─────────┘      └─────────┘      └───────────┘
```

---

## 3. Simulation Components

### 3.1 Order Matching Engine

```python
class PaperTradingEngine:
    """
    Simulates order execution in a realistic market environment.
    """
    
    def __init__(self):
        self.price_feed = PriceFeed()
        self.order_book = OrderBook()
        self.portfolio_tracker = PortfolioTracker()
    
    async def execute_order(
        self,
        order: Order,
        market_conditions: MarketSnapshot
    ) -> ExecutionResult:
        """
        Simulate order execution.
        """
        # Get current price
        current_price = await self.price_feed.get_price(
            order.symbol
        )
        
        # Calculate execution price with slippage
        execution_price = self._calculate_slippage(
            order=order,
            market_price=current_price,
            market_conditions=market_conditions
        )
        
        # Apply commission
        commission = self._calculate_commission(order, execution_price)
        
        # Update portfolio
        await self.portfolio_tracker.record_transaction(
            order=order,
            execution_price=execution_price,
            commission=commission
        )
        
        return ExecutionResult(
            order_id=order.id,
            execution_price=execution_price,
            commission=commission,
            timestamp=datetime.utcnow()
        )
    
    def _calculate_slippage(
        self,
        order: Order,
        market_price: Decimal,
        market_conditions: MarketSnapshot
    ) -> Decimal:
        """
        Calculate realistic slippage based on order size and volatility.
        """
        base_slippage = Decimal('0.001')  # 0.1% base
        
        # Size impact
        size_factor = order.quantity / market_conditions.avg_volume
        size_slippage = base_slippage * Decimal(str(size_factor))
        
        # Volatility impact
        vol_factor = market_conditions.volatility / Decimal('0.20')
        vol_slippage = base_slippage * vol_factor
        
        # Direction (worse for market orders)
        if order.order_type == OrderType.MARKET:
            market_slippage = Decimal('0.002')
        else:
            market_slippage = Decimal('0.0005')
        
        total_slippage = base_slippage + size_slippage + vol_slippage + market_slippage
        
        # Apply to market price
        if order.side == OrderSide.BUY:
            return market_price * (1 + total_slippage)
        else:
            return market_price * (1 - total_slippage)
```

### 3.2 Portfolio Simulation

```python
class SimulatedPortfolio:
    """
    Tracks a paper trading portfolio.
    """
    
    def __init__(self, user_id: UUID, initial_cash: Decimal):
        self.user_id = user_id
        self.cash = initial_cash
        self.positions: Dict[str, Position] = {}
        self.transactions: List[Transaction] = []
        self.value_history: List[PortfolioSnapshot] = []
    
    async def execute_buy(
        self,
        symbol: str,
        quantity: Decimal,
        price: Decimal,
        commission: Decimal
    ) -> None:
        """Execute buy order."""
        total_cost = (price * quantity) + commission
        
        if total_cost > self.cash:
            raise InsufficientFundsError()
        
        self.cash -= total_cost
        
        # Update position
        if symbol in self.positions:
            position = self.positions[symbol]
            position.quantity += quantity
            position.avg_price = self._calculate_new_avg(
                position, quantity, price
            )
        else:
            self.positions[symbol] = Position(
                symbol=symbol,
                quantity=quantity,
                avg_price=price
            )
    
    async def execute_sell(
        self,
        symbol: str,
        quantity: Decimal,
        price: Decimal,
        commission: Decimal
    ) -> None:
        """Execute sell order."""
        if symbol not in self.positions:
            raise PositionNotFoundError()
        
        position = self.positions[symbol]
        if quantity > position.quantity:
            raise InsufficientPositionError()
        
        proceeds = (price * quantity) - commission
        self.cash += proceeds
        
        # Update position
        position.quantity -= quantity
        if position.quantity == 0:
            del self.positions[symbol]
    
    async def get_current_value(self) -> Decimal:
        """Calculate current portfolio value."""
        positions_value = Decimal('0')
        
        for symbol, position in self.positions.items():
            current_price = await self.price_feed.get_price(symbol)
            positions_value += position.quantity * current_price
        
        return self.cash + positions_value
```

---

## 4. Backtesting Engine

### 4.1 Backtest Runner

```python
class BacktestEngine:
    """
    Run strategies against historical data.
    """
    
    def __init__(self):
        self.price_data = HistoricalPriceRepository()
        self.event_log = EventLogger()
    
    async def run_backtest(
        self,
        strategy: Strategy,
        start_date: datetime,
        end_date: datetime,
        initial_capital: Decimal
    ) -> BacktestResult:
        """
        Run strategy against historical data.
        """
        # Initialize
        portfolio = SimulatedPortfolio(
            user_id=strategy.user_id,
            initial_cash=initial_capital
        )
        
        # Get historical data
        price_data = await self.price_data.get_range(
            symbols=strategy.universe,
            start_date=start_date,
            end_date=end_date
        )
        
        # Simulation loop
        for timestamp, prices in price_data:
            market_snapshot = MarketSnapshot(
                timestamp=timestamp,
                prices=prices
            )
            
            # Run strategy
            signals = await strategy.generate_signals(
                portfolio=portfolio,
                market_data=market_snapshot
            )
            
            # Execute signals
            for signal in signals:
                await self._execute_signal(
                    signal=signal,
                    portfolio=portfolio,
                    market_data=market_snapshot
                )
            
            # Record snapshot
            await portfolio.record_snapshot(timestamp)
        
        # Calculate metrics
        return self._calculate_metrics(portfolio)
    
    def _calculate_metrics(
        self,
        portfolio: SimulatedPortfolio
    ) -> BacktestResult:
        """Calculate performance metrics."""
        returns = self._calculate_returns(portfolio)
        
        return BacktestResult(
            total_return=returns.total_return,
            annualized_return=returns.annualized,
            volatility=returns.volatility,
            sharpe_ratio=returns.sharpe,
            max_drawdown=returns.max_drawdown,
            win_rate=returns.win_rate,
            profit_factor=returns.profit_factor,
            transactions=portfolio.transactions,
            equity_curve=portfolio.value_history
        )
```

---

## 5. Metrics and Reporting

### 5.1 Performance Metrics

| Metric | Formula | Description |
|----------|---------|-------------|
| Total Return | (End - Start) / Start | Overall performance |
| Annualized Return | (1 + TR)^(365/D) - 1 | Normalized return |
| Volatility | StdDev(daily returns) * sqrt(252) | Risk measure |
| Sharpe Ratio | (Return - Risk Free) / Volatility | Risk-adjusted return |
| Max Drawdown | Max peak-to-trough decline | Worst loss period |
| Win Rate | Wins / Total Trades | Success rate |
| Profit Factor | Gross Profit / Gross Loss | Profit efficiency |

### 5.2 Report Generation

```python
class BacktestReport:
    """
    Generate comprehensive backtest reports.
    """
    
    def generate(self, result: BacktestResult) -> Report:
        """Generate PDF report with charts."""
        return Report(
            summary=self._generate_summary(result),
            equity_chart=self._plot_equity_curve(result),
            drawdown_chart=self._plot_drawdowns(result),
            monthly_returns=self._generate_monthly_table(result),
            trade_list=self._generate_trade_list(result),
            statistics=self._generate_statistics(result)
        )
```

---

## 6. Document Information

| Field | Value |
|-------|-------|
| Document ID | AFIP-DOC-011 |
| Version | 1.0.0 |
| Status | Draft |

---

## Next Document

**→ Continue to**: [12_Risk_Management.md](./12_Risk_Management.md)  
**← Back to**: [10_API_Architecture.md](./10_API_Architecture.md)
