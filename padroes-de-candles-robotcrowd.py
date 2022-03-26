alta = (C0) > (O0) #candle de alta
baixa = (C0) < (O0) #candle de baixa
cog_alta = (C0) < (O0) & (C1) > (O1) #candle de baixa seguido de candle de alta
cog_baixa = (C0) > (O0) & (C1) < (O1) #candle de alta seguido de candle de baixa
cogm_alta = (C0) < (O0) & (C1) > (O1) & (L0) == (H1) #candle de baixa seguido de candle de alta
cogm_baixa = (C0) > (O0) & (C1) < (O1) & (L1) == (H0) #candle de alta seguido de candle de baixa
