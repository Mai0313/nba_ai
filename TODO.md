透過 nba_api 套件取得以下資訊

數據維度,具體資訊 (Features),nba_api 支援度,對應的 Endpoint (模組)
基礎數據,得分、籃板、助攻、命中率、上場時間,✅ 完美支援,"playergamelogs, leaguegamefinder"
高階數據,USG% (使用率)、Net Rating、TS% (真實命中率),✅ 完美支援,leaguedashplayerstats (設為 Advanced)
球員狀態,出勤率 (GP/GS)、生涯傷病頻率、輪休紀錄,⚠️ 部份支援,"commonplayerinfo, playergamelogs"
賽程負荷,休息天數 (Rest Days)、是否為 B2B、賽季進度,🛠️ 需自行計算,leaguegamefinder (需計算兩場 GameDate 差)
球隊環境,隊友缺陣時的數據變化 (On/Off Court),✅ 支援,teamplayeronoffdetails
