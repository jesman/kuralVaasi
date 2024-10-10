# ஒலி உருவாக்கி  [![twitter][1.1]][1] [![facebook][1.2]][2] [![google+][1.3]][3] [![linkedin][1.4]][4]

[1.1]: http://www.tensorlet.org/wp-content/uploads/2021/01/button_twitter_22x22.png
[1.2]: http://www.tensorlet.org/wp-content/uploads/2021/01/facebook-button_22x22.png
[1.3]: http://www.tensorlet.org/wp-content/uploads/2021/01/button_google_22.xx_.png
[1.4]: http://www.tensorlet.org/wp-content/uploads/2021/01/button_linkedin_22x22.png

[1]: https://twitter.com/intent/tweet?text=FinRL-Financial-Deep-Reinforcement-Learning%20&url=https://github.com/jesman/kuralreadTamil&hashtags=DRL&hashtags=AI
[2]: https://www.facebook.com/sharer.php?u=http%3A%2F%2Fgithub.com%2FAI4Finance-Foundation%2FFinRL
[3]: https://plus.google.com/share?url=https://github.com/jesman/kuralreadTamil
[4]: https://www.linkedin.com/sharing/share-offsite/?url=http%3A%2F%2Fgithub.com%2FAI4Finance-Foundation%2FFinRL

<div align="center">
<img align="center" src=figs/logo_transparent_background.png width="55%"/>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


## Outline

- [Overview](#Overview)
- [File Structure](#File-Structure)
- [Supported Data Sources](#Supported-Data-Sources)
- [Installation](#Installation)
- [Status Update](#Status-Update)
- [Tutorials](#Tutorials)
- [Publications](#Publications)
- [News](#News)
- [Citing FinRL](#Citing-FinRL)
- [Welcome Contributions](#To-Contribute)
- [Sponsorship](#Sponsorship)
- [LICENSE](#LICENSE)

## Overview

FinRL has three layers: market environments, agents, and applications.  For a trading task (on the top), an agent (in the middle) interacts with a market environment (at the bottom), making sequential decisions.

<div align="center">
<img align="center" src=figs/finrl_framework.png>
</div>

A quick start: Stock_NeurIPS2018.ipynb. Videos [FinRL](http://www.youtube.com/watch?v=ZSGJjtM-5jA) at [AI4Finance Youtube Channel](https://www.youtube.com/channel/UCrVri6k3KPBa3NhapVV4K5g).


## File Structure
<a
The main folder 
.
├── audios
│   ├── அன்பிற்கும்_உண்டோ.mp3
│   ├── ஒலிக்கோப்பு_உருவாக்கி.mp3
│   └── செல்லாமை_உண்டேல்.mp3
├── data
│   ├── kural_tam.txt
│   ├── kural.txt
│   └── LICENSE
├── equalizer.py
├── Guide.md
├── Guide.pdf
├── help.py
├── images
│   ├── Create_audio_MP3.png
│   ├── help.png
│   ├── main_app.png
│   ├── Open_and_Play.png
│   └── search_kural.png
├── LICENSE
├── main.py
├── mp3_generator.py
├── __pycache__
│   ├── equalizer.cpython-310.pyc
│   ├── help.cpython-310.pyc
│   └── mp3_generator.cpython-310.pyc
├── README.md
├── res
│   ├── Guide.md
│   └── Guide.pdf
├── அன்பிற்கும்_உண்டோ.mp3
├── மென்பொருள்_வழிகாட்டி.md
└── வேண்டுதல்_வேண்டாமை.mp3
/a>

## Supported Data Sources

|Data Source |Type |Range and Frequency |Request Limits|Raw Data|Preprocessed Data|
|  ----  |  ----  |  ----  |  ----  |  ----  |  ----  |
|[Akshare](https://alpaca.markets/docs/introduction/)| CN Securities| 2015-now, 1day| Account-specific| OHLCV| Prices&Indicators|
|[Alpaca](https://alpaca.markets/docs/introduction/)| US Stocks, ETFs| 2015-now, 1min| Account-specific| OHLCV| Prices&Indicators|
|[Baostock](http://baostock.com/baostock/index.php/Python_API%E6%96%87%E6%A1%A3)| CN Securities| 1990-12-19-now, 5min| Account-specific| OHLCV| Prices&Indicators|
|[Binance](https://binance-docs.github.io/apidocs/spot/en/#public-api-definitions)| Cryptocurrency| API-specific, 1s, 1min| API-specific| Tick-level daily aggegrated trades, OHLCV| Prices&Indicators|
|[CCXT](https://docs.ccxt.com/en/latest/manual.html)| Cryptocurrency| API-specific, 1min| API-specific| OHLCV| Prices&Indicators|
|[EODhistoricaldata](https://eodhistoricaldata.com/financial-apis/)| US Securities| Frequency-specific, 1min| API-specific | OHLCV | Prices&Indicators|
|[IEXCloud](https://iexcloud.io/docs/api/)| NMS US securities|1970-now, 1 day|100 per second per IP|OHLCV| Prices&Indicators|
|[JoinQuant](https://www.joinquant.com/)| CN Securities| 2005-now, 1min| 3 requests each time| OHLCV| Prices&Indicators|
|[QuantConnect](https://www.quantconnect.com/docs/home/home)| US Securities| 1998-now, 1s| NA| OHLCV| Prices&Indicators|
|[RiceQuant](https://www.ricequant.com/doc/rqdata/python/)| CN Securities| 2005-now, 1ms| Account-specific| OHLCV| Prices&Indicators|
|[Tushare](https://tushare.pro/document/1?doc_id=131)| CN Securities, A share| -now, 1 min| Account-specific| OHLCV| Prices&Indicators|
|[WRDS](https://wrds-www.wharton.upenn.edu/pages/about/data-vendors/nyse-trade-and-quote-taq/)| US Securities| 2003-now, 1ms| 5 requests each time| Intraday Trades|Prices&Indicators|
|[YahooFinance](https://pypi.org/project/yfinance/)| US Securities| Frequency-specific, 1min| 2,000/hour| OHLCV | Prices&Indicators|














