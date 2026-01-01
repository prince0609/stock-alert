import yfinance as yf
import pandas as pd
import pandas_ta as ta
import streamlit as st

# ================= CONFIG =================

# SYMBOLS = ["360ONE.NS",
#     "ABB.NS",
#     "APLAPOLLO.NS",
#     "AUBANK.NS",
#     "ADANIENSOL.NS",
#     "ADANIENT.NS",
#     "ADANIGREEN.NS",
#     "ADANIPORTS.NS",
#     "ABCAPITAL.NS",
#     "ALKEM.NS",
#     "AMBER.NS",
#     "AMBUJACEM.NS",
#     "ANGELONE.NS",
#     "APOLLOHOSP.NS",
#     "ASHOKLEY.NS",
#     "ASIANPAINT.NS",]

SYMBOLS = [
    "360ONE.NS",
    "ABB.NS",
    "APLAPOLLO.NS",
    "AUBANK.NS",
    "ADANIENSOL.NS",
    "ADANIENT.NS",
    "ADANIGREEN.NS",
    "ADANIPORTS.NS",
    "ABCAPITAL.NS",
    "ALKEM.NS",
    "AMBER.NS",
    "AMBUJACEM.NS",
    "ANGELONE.NS",
    "APOLLOHOSP.NS",
    "ASHOKLEY.NS",
    "ASIANPAINT.NS",
    "ASTRAL.NS",
    "AUROPHARMA.NS",
    "DMART.NS",
    "AXISBANK.NS",
    "BSE.NS",
    "BAJAJ-AUTO.NS",
    "BAJFINANCE.NS",
    "BAJAJFINSV.NS",
    "BAJAJHLDNG.NS",
    "BANDHANBNK.NS",
    "BANKBARODA.NS",
    "BANKINDIA.NS",
    "BDL.NS",
    "BEL.NS",
    "BHARATFORG.NS",
    "BHEL.NS",
    "BPCL.NS",
    "BHARTIARTL.NS",
    "BIOCON.NS",
    "BLUESTARCO.NS",
    "BOSCHLTD.NS",
    "BRITANNIA.NS",
    "CGPOWER.NS",
    "CANBK.NS",
    "CDSL.NS",
    "CHOLAFIN.NS",
    "CIPLA.NS",
    "COALINDIA.NS",
    "COFORGE.NS",
    "COLPAL.NS",
    "CAMS.NS",
    "CONCOR.NS",
    "CROMPTON.NS",
    "CUMMINSIND.NS",
    "DLF.NS",
    "DABUR.NS",
    "DALBHARAT.NS",
    "DELHIVERY.NS",
    "DIVISLAB.NS",
    "DIXON.NS",
    "DRREDDY.NS",
    "ETERNAL.NS",
    "EICHERMOT.NS",
    "EXIDEIND.NS",
    "NYKAA.NS",
    "FORTIS.NS",
    "GAIL.NS",
    "GMRAIRPORT.NS",
    "GLENMARK.NS",
    "GODREJCP.NS",
    "GODREJPROP.NS",
    "GRASIM.NS",
    "HCLTECH.NS",
    "HDFCAMC.NS",
    "HDFCBANK.NS",
    "HDFCLIFE.NS",
    "HAVELLS.NS",
    "HEROMOTOCO.NS",
    "HINDALCO.NS",
    "HAL.NS",
    "HINDPETRO.NS",
    "HINDUNILVR.NS",
    "HINDZINC.NS",
    "POWERINDIA.NS",
    "HUDCO.NS",
    "ICICIBANK.NS",
    "ICICIGI.NS",
    "ICICIPRULI.NS",
    "IDFCFIRSTB.NS",
    "IIFL.NS",
    "ITC.NS",
    "INDIANB.NS",
    "IEX.NS",
    "IOC.NS",
    "IRCTC.NS",
    "IRFC.NS",
    "IREDA.NS",
    "INDUSTOWER.NS",
    "INDUSINDBK.NS",
    "NAUKRI.NS",
    "INFY.NS",
    "INOXWIND.NS",
    "INDIGO.NS",
    "JINDALSTEL.NS",
    "JSWENERGY.NS",
    "JSWSTEEL.NS",
    "JIOFIN.NS",
    "JUBLFOOD.NS",
    "KEI.NS",
    "KPITTECH.NS",
    "KALYANKJIL.NS",
    "KAYNES.NS",
    "KFINTECH.NS",
    "KOTAKBANK.NS",
    "LTF.NS",
    "LICHSGFIN.NS",
    "LTIM.NS",
    "LT.NS",
    "LAURUSLABS.NS",
    "LICI.NS",
    "LODHA.NS",
    "LUPIN.NS",
    "M&M.NS",
    "MANAPPURAM.NS",
    "MANKIND.NS",
    "MARICO.NS",
    "MARUTI.NS",
    "MFSL.NS",
    "MAXHEALTH.NS",
    "MAZDOCK.NS",
    "MPHASIS.NS",
    "MCX.NS",
    "MUTHOOTFIN.NS",
    "NBCC.NS",
    "NHPC.NS",
    "NMDC.NS",
    "NTPC.NS",
    "NATIONALUM.NS",
    "NESTLEIND.NS",
    "NUVAMA.NS",
    "OBEROIRLTY.NS",
    "ONGC.NS",
    "OIL.NS",
    "PAYTM.NS",
    "OFSS.NS",
    "POLICYBZR.NS",
    "PGEL.NS",
    "PIIND.NS",
    "PNBHOUSING.NS",
    "PAGEIND.NS",
    "PATANJALI.NS",
    "PERSISTENT.NS",
    "PETRONET.NS",
    "PIDILITIND.NS",
    "PPLPHARMA.NS",
    "POLYCAB.NS",
    "PFC.NS",
    "POWERGRID.NS",
    "PREMIERENE.NS",
    "PRESTIGE.NS",
    "PNB.NS",
    "RBLBANK.NS",
    "RECLTD.NS",
    "RVNL.NS",
    "RELIANCE.NS",
    "SBICARD.NS",
    "SBILIFE.NS",
    "SHREECEM.NS",
    "SRF.NS",
    "SAMMAANCAP.NS",
    "MOTHERSON.NS",
    "SHRIRAMFIN.NS",
    "SIEMENS.NS",
    "SOLARINDS.NS",
    "SONACOMS.NS",
    "SBIN.NS",
    "SAIL.NS",
    "SUNPHARMA.NS",
    "SUPREMEIND.NS",
    "SUZLON.NS",
    "SWIGGY.NS",
    "SYNGENE.NS",
    "TATACONSUM.NS",
    "TVSMOTOR.NS",
    "TCS.NS",
    "TATAELXSI.NS",
    "TMPV.NS",
    "TATAPOWER.NS",
    "TATASTEEL.NS",
    "TATATECH.NS",
    "TECHM.NS",
    "FEDERALBNK.NS",
    "INDHOTEL.NS",
    "PHOENIXLTD.NS",
    "TITAN.NS",
    "TORNTPHARM.NS",
    "TORNTPOWER.NS",
    "TRENT.NS",
    "TIINDIA.NS",
    "UNOMINDA.NS",
    "UPL.NS",
    "ULTRACEMCO.NS",
    "UNIONBANK.NS",
    "UNITDSPR.NS",
    "VBL.NS",
    "VEDL.NS",
    "IDEA.NS",
    "VOLTAS.NS",
    "WAAREEENER.NS",
    "WIPRO.NS",
    "YESBANK.NS",
    "ZYDUSLIFE.NS"
]


INTERVAL = "5m"
PERIOD = "5d"
SuperTrend_LENGTH = 20
SuperTrend_MULT = 2
# =========================================

st.set_page_config(page_title="Algo Scanner", layout="wide")
st.title("📊 Indian Market Algo Scanner")

# ---------------- DATA FUNCTIONS ----------------
@st.cache_data(ttl=300)
def fetch_data(symbol):
    df = yf.download(
        symbol,
        interval=INTERVAL,
        period=PERIOD,
        progress=False
    )

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df = df.dropna()

    # 🔧 TIMEZONE FIX: UTC → IST
    if df.index.tz is None:
        df.index = df.index.tz_localize("UTC").tz_convert("Asia/Kolkata")
    else:
        df.index = df.index.tz_convert("Asia/Kolkata")

    # Optional: remove timezone info for clean display
    df.index = df.index.tz_localize(None)

    return df


def apply_indicators(df):
    # ---- EMAs ----
    df["EMA8"] = ta.ema(df["Close"], length=8)
    df["EMA30"] = ta.ema(df["Close"], length=30)

    # ---- SuperTrend ----
    st_df = ta.supertrend(
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        length=SuperTrend_LENGTH,
        multiplier=SuperTrend_MULT
    )
    df = pd.concat([df, st_df], axis=1)

    # ---- MACD ----
    macd = ta.macd(df["Close"])
    df = pd.concat([df, macd], axis=1)

    # ---- ADX (Trend Strength) ----
    adx = ta.adx(
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        length=14
    )
    df = pd.concat([df, adx], axis=1)

    return df

# ---------------- STRATEGIES ----------------
def supertrend_macd(symbol):
    df = fetch_data(symbol)
    df = apply_indicators(df)

    if len(df) < 60:
        return "NO SETUP", None, None

    st_col = f"SUPERTd_{SuperTrend_LENGTH}_{SuperTrend_MULT}"
    macd_col = "MACD_12_26_9"
    signal_col = "MACDs_12_26_9"

    curr = df.iloc[-1]
    recent = df.iloc[-5:-1]   # previous 4 candles

    signal_time = None
    signal_type = None

    # ===== CHECK BUY SETUP =====
    for i in range(1, len(recent)):
        st_flip = (
            recent.iloc[i-1][st_col] == -1 and
            recent.iloc[i][st_col] == 1
        )

        macd_cross = (
            recent.iloc[i-1][macd_col] <= recent.iloc[i-1][signal_col]
            and recent.iloc[i][macd_col] > recent.iloc[i][signal_col]
        )

        if st_flip and macd_cross:
            if curr[st_col] == 1 and curr[macd_col] > curr[signal_col]:
                signal_time = recent.iloc[i].name
                signal_type = "BUY"
            break

    # ===== CHECK SELL SETUP =====
    if signal_type is None:
        for i in range(1, len(recent)):
            st_flip = (
                recent.iloc[i-1][st_col] == 1 and
                recent.iloc[i][st_col] == -1
            )

            macd_cross = (
                recent.iloc[i-1][macd_col] >= recent.iloc[i-1][signal_col]
                and recent.iloc[i][macd_col] < recent.iloc[i][signal_col]
            )

            if st_flip and macd_cross:
                if curr[st_col] == -1 and curr[macd_col] < curr[signal_col]:
                    signal_time = recent.iloc[i].name
                    signal_type = "SELL"
                break

    if signal_type:
        return signal_type, signal_time, curr["ADX_14"]

    return "NO SETUP", None, None



def ema_8_30(symbol):
    df = fetch_data(symbol)
    df = apply_indicators(df)

    if len(df) < 50:
        return "NO SETUP", None, None

    curr = df.iloc[-1]
    recent = df.iloc[-5:-1]   # previous 4 candles

    signal_time = None
    signal_type = None

    # ===== BUY SETUP =====
    for i in range(1, len(recent)):
        if (
            recent.iloc[i-1]["EMA8"] <= recent.iloc[i-1]["EMA30"]
            and recent.iloc[i]["EMA8"] > recent.iloc[i]["EMA30"]
        ):
            if curr["EMA8"] > curr["EMA30"] and curr["Close"] > curr["EMA30"]:
                signal_time = recent.iloc[i].name
                signal_type = "BUY"
            break

    # ===== SELL SETUP =====
    if signal_type is None:
        for i in range(1, len(recent)):
            if (
                recent.iloc[i-1]["EMA8"] >= recent.iloc[i-1]["EMA30"]
                and recent.iloc[i]["EMA8"] < recent.iloc[i]["EMA30"]
            ):
                if curr["EMA8"] < curr["EMA30"] and curr["Close"] < curr["EMA30"]:
                    signal_time = recent.iloc[i].name
                    signal_type = "SELL"
                break

    if signal_type:
        return signal_type, signal_time, curr["ADX_14"]

    return "NO SETUP", None, None
# ---------------- UI ----------------
run = st.button("🔄 Scan Market")

col1, col2 = st.columns(2)

if run:
    st_macd = []
    ema_results = []

    with st.spinner("Scanning stocks..."):
        for sym in SYMBOLS:
            signal, t, adx = supertrend_macd(sym)
            st_macd.append({
                "Stock": sym,
                "Signal": signal,
                "ADX": adx,
                "Time": t.strftime("%d-%m %H:%M") if t else "-"
            })

            signal, t, adx = ema_8_30(sym)
            ema_results.append({
                "Stock": sym,
                "Signal": signal,
                "ADX": adx,
                "Time": t.strftime("%d-%m %H:%M") if t else "-"
            })
        
        st_macd = [
            row for row in st_macd
            if row["Signal"] in ("BUY", "SELL")
        ]

        ema_results = [
            row for row in ema_results
            if row["Signal"] in ("BUY", "SELL")
        ]

    with col1:
        st.subheader("📉 SuperTrend + MACD")
        df1 = pd.DataFrame(st_macd)
        st.dataframe(
            df1.style.applymap(
                lambda x: "color: green" if x == "BUY"
                else "color: red" if x == "SELL"
                else "color: grey",
                subset=["Signal"]
            ),
            use_container_width=True
        )

    with col2:
        st.subheader("📈 EMA 8–30 Strategy")
        df2 = pd.DataFrame(ema_results)
        st.dataframe(
            df2.style.applymap(
                lambda x: "color: green" if x == "BUY"
                else "color: red" if x == "SELL"
                else "color: grey",
                subset=["Signal"]
            ),
            use_container_width=True
        )
