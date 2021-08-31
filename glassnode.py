# %%
import json
import requests
import iso8601
import pandas as pd
import datetime
# %%

URLS = {'Indicators':'https://api.glassnode.com/v1/metrics/indicators/',
        'Market':'https://api.glassnode.com/v1/metrics/market/',
        'Mining':'https://api.glassnode.com/v1/metrics/mining/',
        'Supply':'https://api.glassnode.com/v1/metrics/supply/',
        'Addresses':'https://api.glassnode.com/v1/metrics/addresses/',
        'Transactions':'https://api.glassnode.com/v1/metrics/transactions/',
        'Blockchain':'https://api.glassnode.com/v1/metrics/blockchain/',
        'Derivatives':'https://api.glassnode.com/v1/metrics/derivatives/',
        'Distribution':'https://api.glassnode.com/v1/metrics/distribution/',
        'Entities':'https://api.glassnode.com/v1/metrics/entities/',
        'Institutions':'https://api.glassnode.com/v1/metrics/institutions/'}

# %%
Indicators = ['rhodl_ratio',
              'cvdd',
              'balanced_price_usd',
              'hash_ribbon',
              'difficulty_ribbon',
              'difficulty_ribbon_compression',
              'nvt',
              'nvts',
              'velocity',
              'nvt_entity_adjusted',
              'cdd_supply_adjusted',
              'cdd_supply_adjusted_binary',
              'average_dormancy_supply_adjusted',
              'spent_output_price_distribution_ath',
              'spent_output_price_distribution_percent',
              'puell_multiple',
              'sopr_adjusted',
              'reserve_risk',
              'sopr_less_155',
              'sopr_more_155',
              'hodler_net_position_change',
              'hodled_lost_coins',
              'cyd',
              'cyd_supply_adjusted',
              'cyd_account_based',
              'cyd_account_based_supply_adjusted',
              'cdd90_age_adjusted',
              'cdd90_account_based_age_adjusted',
              'sopr',
              'cdd',
              'asol',
              'msol',
              'average_dormancy',
              'liveliness',
              'unrealized_profit',
              'unrealized_loss',
              'net_unrealized_profit_loss',
              'nupl_less_155',
              'nupl_more_155',
              'sopr_account_based',
              'cdd_account_based',
              'asol_account_based',
              'msol_account_based',
              'dormancy_account_based',
              'dormancy_flow',
              'liveliness_account_based',
              'mvrv_account_based',
              'rcap_account_based',
              'unrealized_profit_account_based'
              'unrealized_loss_account_based',
              'net_unrealized_profit_loss_account_based',
              'nupl_less_155_account_based',
              'nupl_more_155_account_based',
              'net_realized_profit_loss',
              'realized_profit_loss_ratio',
              'stock_to_flow_ratio',
              'stock_to_flow_deflection',
              'realized_profit',
              'realized_loss',
              'ssr',
              'ssr_oscillator', 
              'utxo_realized_price_distribution_ath',
              'utxo_realized_price_distribution_percent',
              'soab',
              'sol_1h',
              'sol_1h_24h',
              'sol_1d_1w',
              'sol_1w_1m',
              'sol_1m_3m',
              'sol_3m_6m', 
              'sol_6m_12m',
              'sol_1y_2y',
              'sol_2y_3y',
              'sol_3y_5y',
              'sol_5y_7y',
              'sol_7y_10y',
              'sol_more_10y']
# %%
Market = ['price_usd_ohlc',
          'price_drawdown_relative',
          'deltacap_usd',
          'marketcap_usd',
          'mvrv',
          'marketcap_realized_usd',
          'mvrv_z_score',
          'mvrv_less_155',
          'mvrv_more_155',
          'price_realized_usd']

# %%
Mining = ['difficulty_latest',
          'hash_rate_mean',
          'revenue_sum',
          'revenue_from_fees',
          'volume_mined_sum',
          'miners_outflow_multiple',
          'thermocap',
          'marketcap_thermocap_ratio',
          'miners_unspent_supply']

# %%
Supply = ['liquid_illiquid_sum',
          'liquid_change',
          'illiquid_change',
          'current',
          'issued',
          'inflation_rate',
          'active_24h',
          'active_1d_1w',
          'active_1w_1m',
          'active_1m_3m',
          'active_3m_6m',
          'active_6m_12m',
          'active_1y_2y',
          'active_2y_3y',
          'active_3y_5y',
          'active_5y_7y',
          'active_7y_10y',
          'active_more_10y',
          'hodl_waves',
          'active_more_1y_percent',
          'active_more_2y_percent',
          'active_more_3y_percent',
          'active_more_5y_percent',
          'rcap_hodl_waves',
          'current_adjusted',
          'profit_sum',
          'loss_sum',
          'profit_relative',
          'sth_sum',
          'lth_sum',
          'sth_loss_sum',
          'lth_loss_sum',
          'sth_profit_sum',
          'lth_profit_sum',
          'lth_sth_profit_loss_relative',
          'lth_net_change']

# %%
Addresses = ['sending_to_exchanges_count',
             'receiving_from_exchanges_count',
             'count',
             'sending_count',
             'receiving_count',
             'active_count',
             'new_non_zero_count',
             'accumulation_count',
             'accumulation_balance',
             'non_zero_count',
             'min_point_zero_1_count',
             'min_point_1_count',
             'min_1_count',
             'min_10_count',
             'min_100_count',
             'min_1k_count',
             'min_10k_count',
             'min_32_count',
             'supply_balance_less_0001',
             'supply_balance_0001_001',
             'supply_balance_001_01',
             'supply_balance_01_1',
             'supply_balance_1_10',
             'supply_balance_10_100',
             'supply_balance_100_1k',
             'supply_balance_1k_10k',
             'supply_balance_10k_100k',
             'supply_balance_more_100k',
             'supply_distribution_relative',
             'min_1_usd_count',
             'min_10_usd_count',
             'min_100_usd_count',
             'min_1k_usd_count',
             'min_10k_usd_count',
             'min_100k_usd_count',
             'min_1m_usd_count',
             'profit_count',
             'loss_count',
             'profit_relative']

# %%
Transactions = ['count',
                'rate',
                'contract_calls_external_count',
                'contract_calls_internal_count',
                'size_mean',
                'size_sum',
                'transfers_volume_by_size_entity_adjusted_sum',
                'transfers_volume_by_size_entity_adjusted_relative',
                'transfers_to_otc_desks_count',
                'transfers_from_otc_desks_count',
                'transfers_volume_to_otc_desks_sum',
                'transfers_volume_from_otc_desks_sum',
                'transfers_count',
                'transfers_rate',
                'transfers_volume_sum',
                'transfers_volume_mean',
                'transfers_volume_median',
                'transfers_volume_adjusted_sum',
                'transfers_volume_adjusted_mean',
                'transfers_volume_adjusted_median',
                'transfers_volume_profit_relative',
                'transfers_volume_profit_sum',
                'transfers_volume_loss_sum',
                'entity_adjusted_count',
                'transfers_volume_entity_adjusted_sum',
                'transfers_volume_entity_adjusted_mean',
                'transfers_volume_entity_adjusted_median',
                'transfers_from_miners_count',
                'transfers_to_miners_count',
                'transfers_volume_from_miners_sum',
                'transfers_volume_to_miners_sum',
                'transfers_volume_miners_net',
                'transfers_volume_miners_to_exchanges',
                'transfers_volume_miners_to_exchanges_all',
                'transfers_volume_to_exchanges_mean',
                'transfers_volume_from_exchanges_mean',
                'transfers_volume_exchanges_net',
                'transfers_to_exchanges_count',
                'transfers_from_exchanges_count',
                'transfers_volume_to_exchanges_sum',
                'transfers_volume_from_exchanges_sum']

# %%
Blockchain = ['utxo_count',
              'utxo_created_count',
              'utxo_spent_count',
              'utxo_created_value_sum',
              'utxo_spent_value_sum',
              'utxo_created_value_mean',
              'utxo_spent_value_mean',
              'utxo_created_value_median',
              'utxo_spent_value_median',
              'utxo_profit_count',
              'utxo_loss_count',
              'utxo_profit_relative',
              'block_height',
              'block_count',
              'block_interval_mean',
              'block_interval_median',
              'block_size_mean',
              'block_size_sum',
              '']

# %%
Derivatives = ['futures_funding_rate_perpetual',
               'futures_funding_rate_perpetual_all',
               'futures_open_interest_cash_margin_sum',
               'futures_open_interest_crypto_margin_sum',
               'futures_open_interest_crypto_margin_relative',
               'futures_estimated_leverage_ratio',
               'futures_volume_daily_sum',
               'futures_volume_daily_perpetual_sum',
               'futures_open_interest_sum',
               'futures_open_interest_perpetual_sum',
               'futures_liquidated_volume_short_sum',
               'futures_liquidated_volume_short_mean',
               'futures_liquidated_volume_long_sum',
               'futures_liquidated_volume_long_mean',
               'futures_liquidated_volume_long_relative',
               'futures_volume_daily_sum_all',
               'futures_volume_daily_perpetual_sum_all',
               'futures_open_interest_sum_all',
               'futures_open_interest_perpetual_sum_all',
               'options_volume_daily_sum',
               'options_open_interest_sum',
               'options_open_interest_distribution',
               'futures_open_interest_latest',
               'futures_volume_daily_latest']

# %%
Distribution = ['balance_exchanges','exchange_net_position_change',
                'balance_exchanges_relative','balance_exchanges_all',
                'balance_miners_all','balance_miners_change',
                'balance_otc_desks','balance_1pct_holders',
                'gini','herfindahl','supply_contracts',
                'balance_miners_sum']

# %%
Entities = ['sending_count','receiving_count','active_count','new_count',
            'net_growth_count','min_1k_count','supply_balance_less_0001',
            'supply_balance_0001_001','supply_balance_001_01','supply_balance_01_1',
            'supply_balance_1_10','supply_balance_10_100','supply_balance_100_1k',
            'supply_balance_1k_10k','supply_balance_10k_100k','supply_balance_more_100k',
            'supply_distribution_relative','profit_relative']

# %%
Institutions = ['grayscale_holdings_sum',
                'grayscale_flows_sum',
                'grayscale_premium_percent',
                'grayscale_aum_sum',
                'grayscale_market_price_usd',
                'purpose_etf_holdings_sum',
                'purpose_etf_flows_sum',
                'qbtc_holdings_sum',
                'qbtc_flows_sum',
                'qbtc_premium_percent',
                'qbtc_aum_sum',
                'qbtc_market_price_usd']


# %%
class GlassnodeClient:
    def __init__(self):
        self._api_key = ''
        
    @property
    def api_key(self):
        return self._api_key

    def set_api_key(self, value):
        self._api_key = value

    def get(self, url, a='BTC', i='24h', c='native', s=None, u=None):
        p = dict()
        p['a'] = a
        p['i'] = i
        p['c'] = c

        if s is not None:
            try:
                p['s'] = iso8601.parse_date(s).strftime('%S')
            except iso8601.ParseError:
                p['s'] = s

        if u is not None:
            try:
                p['u'] = iso8601.parse_date(u).strftime('%S')
            except iso8601.ParseError:
                p['u'] = s

        p['api_key'] = self.api_key

        r = requests.get(url, params=p)

        try:
            r.raise_for_status()
        except Exception as e:
            print(e)
            print(r.text)

        try:
            df = pd.DataFrame(json.loads(r.text))
            df = df.set_index('t')
            df.index = pd.to_datetime(df.index, unit='s')
            df = df.sort_index()
            
            if isinstance(df.iloc[0].iloc[0],dict):
                to_df = []
                
                for t in df.index:
                    elem = df.loc[t].iloc[0]
                    elem['t'] = t 
                    to_df.append(elem)
                    
                    s = pd.DataFrame(to_df)
                    s = s.set_index('t')
            else:
                s = df.v
                s.name = '_'.join(url.split('/')[-2:])
        
            return s
        except Exception as e:
            print(e)


# %%
