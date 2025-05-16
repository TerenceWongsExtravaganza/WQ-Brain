PRICES = [
    'open', 'high', 'low', 'close',
    'vwap', 'returns'
]

VOLUMES = [
    'volume', 'adv20', 'cap'
]

one_OP_one = [
    '+', '-', '*', '/', '^'
]

OP_one = [
    '', 'rank', 'sigmoid', 'exp',
    'fraction', 'log', 'log_diff', 'scale',
    'zscore'
]

UNARY_OP = ['', '-']

TS_OP_1D1P = [
    'ts_product', 'ts_std_dev', 'ts_rank',
    'ts_sum', 'ts_entropy', 'ts_av_diff', 'ts_arg_max',
    'ts_decay_linear', 'ts_delay', 'ts_delta', 'ts_ir',
    'ts_max', 'ts_max_diff', 'ts_median', 'ts_min',
    'ts_min_diff', 'ts_skewness', 'ts_kurtosis'

]

TS_OP_1D2P = [
    'ts_corr'
]

GROUP_OP_1D1P = [
    'group_zscore', 'group_std_dev', 'group_rank',
    'group_sum', 'group_scale', 'group_max',
    'group_median'
]

GROUP_DT = [
    'market', 'sector', 'industry', 'subindustry'
]

P_or_M = [
    '', '-'
]

DEAL_WITH_WEIGHT = [
    'rank', 'sigmoid', ''
]

IF_ELSE = [
    '?', ':'
]

CONDITION = [
    '>', '<', '='
]

doubao_fields_1 = [
"ebit /assets", # 资产息税前利润率，衡量企业运用全部资产获取利润的能力
"income /equity", # 净资产收益率，反映股东权益的收益水平
"cashflow_op /liabilities", # 经营活动现金流量对负债的保障程度
"ebitda /interest_expense", # 利息保障倍数，衡量企业支付负债利息的能力
"sales /inventory", # 存货周转率，反映存货的周转速度
"operating_income /revenue", # 营业利润率，体现企业经营活动的盈利能力
"net_income /assets", # 资产净利率，反映资产利用的综合效果
"receivable /sales", # 应收账款周转率，反映应收账款周转速度
"working_capital /current_liabilities", # 营运资本对流动负债的保障程度
"capex /assets", # 资本支出占资产的比例，反映企业的投资力度
"debt /equity", # 资产负债率，衡量企业长期偿债能力
"income_tax /pretax_income", # 税负率，反映企业所承担的税收负担
"rd_expense /revenue", # 研发投入占营收的比例，体现企业对研发的重视程度
"sga_expense /sales", # 销售及管理费用占销售额的比例，反映企业运营成本控制情况
"inventory_turnover * 365 /inventory", # 存货周转天数，衡量存货的变现速度
"return_assets * assets /equity", # 从资产回报率推导权益回报率的一种变形
"return_equity * equity /assets", # 从权益回报率推导资产回报率的一种变形
"operating_expense /revenue", # 营业成本率，衡量企业经营成本在营收中的占比
"liabilities_curr /assets_curr", # 流动比率，衡量企业短期偿债能力
"pretax_income /invested_capital", # 投资回报率，反映投入资本的获利能力
"goodwill /assets", # 商誉占资产的比例，反映企业商誉在总资产中的权重
"sales_growth /sales", # 销售增长率，衡量企业销售的增长情况
"sales_ps * fnd6_csho /sales", # 从每股销售额和总股数推导总销售额的一种变形
"ppent /assets", # 固定资产净值占资产的比例，反映企业固定资产的规模
"interest_expense /debt", # 债务的利息率，反映企业债务融资的成本
"retained_earnings /equity", # 留存收益率，反映企业利润留存的比例
"income_beforeextra /assets", # 剔除特殊项目前的资产收益率，衡量企业正常经营的盈利能力
"cash /liabilities", # 现金对负债的覆盖程度，反映企业即时偿债能力
"capex /sales", # 资本支出占销售额的比例，反映企业对未来发展的投资力度
"inventory /current_assets", # 存货占流动资产的比例，反映企业流动资产的结构
"net_income /invested_capital", # 投资净利率，衡量投入资本获取净收益的能力
"return_assets /return_equity", # 资产回报率与权益回报率的比值，反映权益乘数对回报率的影响
"operating_income /operating_expense", # 营业利润与营业成本的比值，衡量企业经营效益
"liabilities /assets", # 资产负债率的另一种表达，衡量企业的负债水平
"ebit /interest_expense", # 息税前利润对利息的保障倍数，衡量企业支付利息的能力
"income /revenue", # 销售净利率，反映企业销售收入的收益水平
"receivable /current_assets", # 应收账款占流动资产的比例，反映流动资产的质量
"working_capital /assets", # 营运资本占资产的比例，反映企业资产的流动性和偿债能力
"capex /operating_cashflow", # 资本支出与经营活动现金流量的比例，反映企业现金流量对投资的支持能力
"debt /assets", # 资产负债率的另一种表达，衡量企业的负债程度
"income_tax /income", # 净利润的税负率，反映企业净利润所承担的税收负担
"rd_expense /operating_income", # 研发投入对营业利润的占比，反映企业在盈利基础上的研发投入情况
"sga_expense /operating_income", # 销售及管理费用对营业利润的占比，反映运营成本对利润的影响
"inventory_turnover /liabilities_curr", # 存货周转率与流动负债的关系，从存货周转角度看对流动负债的影响
"return_equity /return_assets", # 权益回报率与资产回报率的比值，反映权益杠杆的作用
"operating_expense /operating_income", # 营业成本对营业利润的覆盖倍数，衡量企业盈利空间
"liabilities_curr /current_ratio", # 流动负债与流动比率的关系，从比率角度看流动负债情况
"pretax_income /assets", # 税前资产收益率，衡量企业在税前的资产获利能力
"goodwill /equity", # 商誉占股东权益的比例，反映商誉对股东权益的影响
"sales_growth /invested_capital", # 销售增长率与投入资本的关系，反映投入资本对销售增长的推动作用
"sales_ps /earnings_per_share", # 每股销售额与每股收益的关系，反映企业每股的经营和盈利情况
"ppent /liabilities", # 固定资产净值对负债的比例，反映固定资产对负债的保障程度
"interest_expense /operating_income", # 利息费用对营业利润的占比，反映利息负担对企业盈利的影响
"retained_earnings /assets", # 留存收益占资产的比例，反映企业资产中留存收益的构成
"income_beforeextra /equity", # 剔除特殊项目前的净资产收益率，衡量企业正常经营的股东权益收益水平
"cash /current_liabilities", # 现金对流动负债的保障程度，反映企业短期偿债的即时能力
"capex /net_income", # 资本支出与净利润的比例，反映企业用净利润进行投资的能力
"inventory /liabilities", # 存货对负债的比例，反映存货作为偿债资源的能力
"net_income /operating_income", # 净利润与营业利润的比值，反映企业的盈利质量
"return_assets * equity /assets", # 从资产回报率推导权益相关指标的一种变形
"operating_income /liabilities", # 营业利润对负债的比例，反映企业营业利润对负债的覆盖能力
"liabilities /equity", # 负债权益比，衡量企业财务杠杆的大小
"ebit /assets_curr", # 流动资产的息税前利润率，衡量流动资产的获利能力
"income /assets_curr", # 流动资产收益率，反映流动资产的收益水平
"cashflow_op /assets", # 经营活动现金流量对资产的比例，反映资产产生现金流量的能力
"ebitda /assets", # 资产息税折旧摊销前利润率，衡量企业资产在未扣除折旧摊销前的盈利能力
"sales /receivable", # 应收账款回收期的倒数，反映应收账款回收速度
"working_capital /revenue", # 营运资本对营收的比例，反映营运资本对业务的支持程度
"capex /liabilities_curr", # 资本支出对流动负债的比例，反映流动负债对资本支出的支持能力
"debt /assets_curr", # 流动资产的资产负债率，衡量流动资产的负债水平
"income_tax /operating_income", # 营业利润的税负率，反映营业利润所承担的税收负担
"rd_expense /pretax_income", # 研发投入对税前利润的占比，反映企业在税前利润基础上的研发投入情况
"sga_expense /pretax_income", # 销售及管理费用对税前利润的占比，反映运营成本对税前利润的影响
"inventory_turnover * 365 /sales", # 存货周转天数的另一种计算方式，衡量存货变现速度
"return_equity * assets /equity", # 从权益回报率推导资产相关指标的一种变形
"operating_expense /liabilities", # 营业成本对负债的比例，反映企业营业成本与负债的关系
"liabilities_curr /liabilities", # 流动负债占总负债的比例，反映企业负债的结构
"pretax_income /equity", # 税前净资产收益率，衡量企业在税前的股东权益收益水平
"goodwill /liabilities", # 商誉对负债的比例，反映商誉在企业负债背景下的相对规模
"sales_growth /assets", # 销售增长率对资产的比例，反映资产对销售增长的支持能力
"sales_ps * fnd6_csho /invested_capital", # 从每股销售额和总股数与投入资本的关系，反映投入资本的产出情况
"ppent /equity", # 固定资产净值对股东权益的比例，反映固定资产对股东权益的贡献
"interest_expense /pretax_income", # 利息费用对税前利润的占比，反映利息负担对税前利润的影响
"retained_earnings /liabilities", # 留存收益对负债的比例，反映留存收益对负债的偿还能力
"income_beforeextra /assets_curr", # 剔除特殊项目前的流动资产收益率，衡量企业正常经营的流动资产获利能力
"cash /assets", # 现金占资产的比例，反映企业资产的流动性
"capex /income", # 资本支出对净利润的比例，反映企业用盈利进行投资的情况
"inventory /working_capital", # 存货对营运资本的比例，反映存货在营运资本中的占比
"net_income /liabilities", # 净利润对负债的比例，反映企业净利润对负债的偿还能力
"return_assets * liabilities /assets", # 从资产回报率推导负债相关指标的一种变形
"operating_income /assets_curr", # 流动资产的营业利润率，衡量流动资产的经营效益
"liabilities /assets_curr", # 流动资产的负债比率，衡量流动资产的负债程度
"ebit /liabilities_curr", # 流动负债的息税前利润率，衡量流动负债的获利能力
"income /liabilities_curr", # 流动负债的收益率，反映流动负债的收益水平
"cashflow_op /assets_curr", # 经营活动现金流量对流动资产的比例，反映流动资产产生现金流量的能力
"ebitda /liabilities_curr", # 流动负债的息税折旧摊销前利润率，衡量流动负债在未扣除折旧摊销前的盈利能力
"sales /working_capital", # 营运资本周转率，反映营运资本的利用效率
"capex /operating_income", # 资本支出对营业利润的比例，反映营业利润对资本支出的支持能力
"debt /liabilities_curr", # 流动负债中债务的比例，反映流动负债的构成
"income_tax /net_income", # 净利润的实际税负率，反映企业净利润的税收负担
"rd_expense /sales_growth", # 研发投入对销售增长的比例，反映研发投入对销售增长的推动作用
"sga_expense /sales_growth", # 销售及管理费用对销售增长的比例，反映运营成本对销售增长的影响
"inventory_turnover * 365 /liabilities", # 存货周转天数与负债的关系，从存货周转角度看对负债的影响
"return_equity * liabilities /equity", # 从权益回报率推导负债相关指标的一种变形
"operating_expense /assets_curr", # 流动资产的营业成本率，衡量流动资产的成本水平
"liabilities_curr /working_capital", # 流动负债对营运资本的比例，反映流动负债与营运资本的关系
"pretax_income /assets_curr", # 税前流动资产收益率，衡量企业在税前的流动资产获利能力
"goodwill /assets_curr", # 商誉对流动资产的比例，反映商誉在流动资产中的占比
"sales_growth /liabilities_curr", # 销售增长率对流动负债的比例，反映流动负债对销售增长的支持能力
"sales_ps * fnd6_csho /liabilities", # 从每股销售额和总股数与负债的关系，反映负债的产出情况
"ppent /liabilities_curr", # 固定资产净值对流动负债的比例，反映固定资产对流动负债的保障程度
"interest_expense /net_income", # 利息费用对净利润的占比，反映利息负担对净利润的影响
"retained_earnings /assets_curr", # 留存收益对流动资产的比例，反映留存收益在流动资产中的构成
"income_beforeextra /liabilities_curr", # 剔除特殊项目前的流动负债收益率，衡量企业正常经营的流动负债获利能力
"cash /working_capital", # 现金对营运资本的比例，反映现金在营运资本中的占比
"capex /cashflow_op", # 资本支出对经营活动现金流量的比例，反映经营活动现金流量对资本支出的支持能力
"inventory /current_ratio", # 存货与流动比率的关系，从存货角度看流动比率情况
"net_income /assets_curr", # 流动资产净利率，反映流动资产的综合收益能力
"return_assets * working_capital /assets", # 从资产回报率推导营运资本相关指标的一种变形
"operating_income /working_capital", # 营运资本的营业利润率，衡量营运资本的经营效益
"liabilities /working_capital", # 营运资本的负债比率，衡量营运资本的负债程度
"ebit /working_capital", # 营运资本的息税前利润率，衡量营运资本的获利能力
"income /working_capital", # 营运资本的收益率，反映营运资本的收益水平
"cashflow_op /working_capital", # 经营活动现金流量对营运资本的比例，反映营运资本产生现金流量的能力
"ebitda /working_capital", # 营运资本的息税折旧摊销前利润率，衡量营运资本在未扣除折旧摊销前的盈利能力
"sales /current_ratio", # 销售额与流动比率的关系，从销售角度看流动比率情况
"capex /income_tax", # 资本支出对所得税的比例，反映所得税对资本支出的影响
"debt /working_capital", # 营运资本中债务的比例，反映营运资本的构成
"income_tax /cashflow_op", # 经营活动现金流量的税负率，反映经营活动现金流量所承担的税收负担
"rd_expense /operating_expense", # 研发投入对营业成本的占比，反映营业成本中研发投入的情况
"sga_expense /operating_expense", # 销售及管理费用对营业成本的占比，反映营业成本中运营成本的情况
"inventory_turnover * 365 /working_capital", # 存货周转天数与营运资本的关系，从存货周转角度看对营运资本的影响
"return_equity * working_capital /equity", # 从权益回报率推导营运资本相关指标的一种变形
"operating_expense /working_capital", # 营运资本的营业成本率，衡量营运资本的成本水平
"liabilities_curr /current_ratio * current_assets", # 从流动比率和流动资产推导流动负债的一种变形
"pretax_income /working_capital", # 税前营运资本收益率，衡量企业在税前的营运资本获利能力
"goodwill /working_capital", # 商誉对营运资本的比例，反映商誉在营运资本中的占比
"sales_growth /working_capital", # 销售增长率对营运资本的比例，反映营运资本对销售增长的支持能力
"sales_ps * fnd6_csho /working_capital", # 从每股销售额和总股数与营运资本的关系，反映营运资本的产出情况
"ppent /working_capital", # 固定资产净值对营运资本的比例，反映固定资产对营运资本的贡献
"interest_expense /cashflow_op", # 利息费用对经营活动现金流量的占比，反映利息负担对经营活动现金流量的影响
"retained_earnings /working_capital", # 留存收益对营运资本的比例，反映留存收益在营运资本中的构成
"income_beforeextra /working_capital", # 剔除特殊项目前的营运资本收益率，衡量企业正常经营的营运资本获利能力
"cash /current_ratio * current_assets", # 从流动比率和流动资产推导现金的一种变形
"capex /net_cashflow", # 资本支出对净现金流量（假设存在相关计算或数据）的比例，反映净现金流量对资本支出的支持能力
"inventory /operating_income", # 存货对营业利润的比例，反映存货对营业利润的影响
"net_income /working_capital", # 营运资本的净利润率，反映营运资本的盈利水平
"return_assets * current_assets /assets", # 从资产回报率推导流动资产相关指标的一种变形
"operating_income /current_assets", # 流动资产的营业利润率，衡量流动资产的经营效益
"liabilities /current_assets", # 流动资产的负债比率，衡量流动资产的负债程度
]

research_sent_field = [
'snt1_d1_netrecpercent',
'snt1_d1_analystcoverage',
'snt1_d1_earningsrevision',
    'snt1_d1_downtargetpercent',
    'snt1_cored1_score',
    'snt1_d1_nettargetpercent',
    'snt1_d1_dtstsespe,'
    'snt1_d1_earningssurprise',
    'snt1_d1_buyrecpercent',
    'snt1_d1_fundamentalfocusrank',
    'snt1_d1_uptargetpercent',
    'snt1_d1_sellrecpercent',
    'snt1_d1_longtermepsgrowthest,'
    'snt1_d1_stockrank',
    'snt1_d1_earningstorpedo',
    'snt1_d1_netearningsrevision',
    'snt1_d1_dynamicfocusrank'
]