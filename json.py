# Opening JSON file
import json

f = open('/Users/brahimhamidoudjana/PycharmProjects/APIinterface/APISystem/TSXData.json')

# returns JSON object as
# a dictionary
data = json.load(f)
f.close()
# Iterating through the json
# list
tckr = ['OA14Y', 'OOOTO', 'NQGAH', 'D30SM', 'WHKCN', 'SFNOS', 'M97PA', 'CK2RS', 'X5UV4', 'Y3SCQ', '63Q47', 'Z5HII', 'K8OY9', '477JY', 'NM3VI', '9S971', 'HVR6B', '4OZ9Q', 'HDXPE', 'T2NC5', 'RKG2T', 'DC0OC', '1K95A', 'EOOHV', 'NIKQS', 'GIJQX', 'DBIS8', '1H2XW', 'INTRQ', 'TBHHD', 'XKOBH', '1NTNT', 'Z9T7U', '4FV10', 'GSF45', 'KE4AT', 'BDKV8', 'N06BZ', 'QQIWH', 'FMO8Z', 'ESOQN', 'TGH7Z', 'W2L2K', 'QGY3D', 'P29R0', 'OSFG6', '68HJD', '3PM7N', 'X6HPO', 'QC3VV', 'DK7C9', 'UQJRP', '2A523', 'JU3VN', '5O7XM', 'J7U99', 'DG1L5', '2SCCN', 'DRSQ1', 'QIW70', 'IO9WM', '3K9FF', 'A8DBD', 'J2ZVG', 'SXUH7', 'MSBQE', 'R6NO3', 'H0O4Y', 'KIVN0', 'DFSR3', 'JJO2E', 'Y18QU', '2E1Z7', 'X0W9B', 'VX06Q', 'N89BS', 'DHQW1', 'H08FR', 'MLW24', '8DDW3', 'DD4PJ', 'RXWV0', 'REW2G', 'JAPYC', '07FM5', 'RCC8S', 'RXM4I', 'WOZ4H', 'MDKGT', 'E4EMY', '3GJEG', '0M3Q9', '743BI', 'RYVA0', '6IGMW', 'VV4RV', 'KLSJC', 'BI9DO', '7AYCZ', '6P2Z7', 'PP847', '6OJI9', 'S2HHE', 'TYKAS', 'PCG1F', 'FQZNJ', '2JZXU', '82B1W', 'KKDHF', 'GWKKR', '77EU8', '7856X', 'KMX73', '2Q0FD', '63KJ7', '8G4ZM', 'ZHOXR', 'J2DSO', '05VGI', '4W4SJ', 'CGP24', 'XX9FC', 'NPRMA', '49ZUF', 'J9F86', 'GXD2M', 'LSV4B', 'CVVLM', 'SDM0Q', 'M81BG', 'I55M8', 'FLR5D', 'XW3YP', 'XTJI4', '7Z49Z', 'OO4FH', 'W5CNM', '17XNS', 'NGCB6', 'EDY3Y', 'I3ZJF', 'Z0XOV', '6HZ8X', '3IKP4', 'NSX34', 'DA8AN', 'AEI98', '07PKN', 'OCCXW', '97SHU', '04NT5', 'B2BBT', 'YW8IP', 'H5TKL', 'ZT7MV', '0AXAX', 'RXCBJ', '3UF94', 'AP9SH', 'P89LZ', 'SGKWB', '4EZV0', 'PJK2B', 'JYZP1', '8U6MA', 'ZZLI1', 'KYCHB', 'QSN23', 'M80HL', 'B2P2L', 'FQ8I3', 'CLM2C', 'K6VB3', 'PN2Y3', 'YEM5X', 'QF3MH', 'BK5FF', 'VC0ST', '273FF', 'SLRY6', 'GUJV7', '07P3R', 'WCW7U', '7JI0F', '7085W', 'B9ER3', 'SARU9', 'ZASDH', 'FE7FX', 'EQAHW', 'DSBUK', '3UJ93', '38KEZ', 'YPH8K', 'NNFLA', 'MB888', 'DGX7H', 'VBFLR', '4UI7N', 'BQ81A', 'H2CQG', 'AXZXA', 'K8OGC', 'MP0A4', 'HORHB', 'UYV1T', 'L7NFC', '0FQWH', 'IBPX6', 'TARUQ', 'LPNMA', 'UND9L', 'ZQ5NU', 'ONU44', 'FXXMN', 'WD5YB', 'KK9VJ', 'ZWOKH', 'HO2UT', 'KD4U7', '0DXM8', 'MEM36', 'O4E9V', '3Q2GC', '7B8MF', 'UR74Y', 'EK4PT', 'WC3L6', 'YRNWS', 'UCXHQ', '8SA1Q', '8OS7B', 'KGJUJ', 'YG3NZ', 'CUA7I', 'CDHDC', 'WR61I', 'N657S', 'TJBWU', 'BCYIU', 'EDDV2', 'BQASA', 'JBMZR', 'FGVVB', '6ROLO', 'QJE22', '2HP22', 'RAFZQ', 'P9R4S', 'GKP9Q', 'VQDGA', '5458X', '5D3J7', '327E9', 'GX8UC', 'JHHAX', 'WXXDD', '3V1TO', 'CDOT1', '77ZRO', 'KGRYN', 'S3804', 'EE8QO', 'V2B2V', 'EA75T', 'SDSLC', 'JWD3J', 'PVSZO', 'ESR8U', '5WLDS', '6O76Y', 'FO26M', '6PBK7', '4OIHS', 'SVKGQ', 'LXBHL', 'K5CJB', '1RUT9', '49QF0', 'ULCVN', 'VYSQY', 'M97OU', 'KGXG2', 'L8KDV', 'UUVPH', 'QHO1G', '6IBFY', 'NNC8E', 'KCNVG', '7FXH3', '6WWQB', 'H08RJ', 'KYBJO', 'H0GST', 'F628S', 'EY09Y', 'NF4LF', '7DGIM', '240ZV', 'C4340', '85MML', 'DXFMF', 'DH29W', 'Y26PN', 'S1Y41']

trades = []
temp = [{
        "TimeStamp": "2023-01-06 09:28:00.011058962",
        "TimeStampEpoch": "1673015280011058962",
        "Direction": "NBFToExchange",
        "OrderID": "b963bbc8-9283-11ed-9ad4-047c16291a22",
        "MessageType": "NewOrderRequest",
        "Symbol": "OA14Y",
        "OrderPrice": 61.56,
        "Exchange": "TSX"
    },
    {
        "TimeStamp": "2023-01-06 09:28:00.011081372",
        "TimeStampEpoch": "1673015280011081372",
        "Direction": "NBFToExchange",
        "OrderID": "b963bbc9-9283-11ed-8b08-047c16291a22",
        "MessageType": "NewOrderRequest",
        "Symbol": "OOOTO",
        "OrderPrice": 69.37,
        "Exchange": "TSX"
    },
    {
        "TimeStamp": "2023-01-06 09:28:00.011117286",
        "TimeStampEpoch": "1673015280011117286",
        "Direction": "ExchangeToNBF",
        "OrderID": "b963bbc8-9283-11ed-9ad4-047c16291a22",
        "MessageType": "NewOrderAcknowledged",
        "Symbol": "OA14Y",
        "OrderPrice": 61.56,
        "Exchange": "TSX"
    }]

for i in data:
   if i["Symbol"] == "OA14Y":
       temp.append(i)
print(len(temp))

i = 0
with open("OA14Y.json", "w") as outfile:
    # json.dumps(temp[0])
    json.dump(temp[0], outfile)
    print(i)
    i = i +1
    # print(t)

print(temp)


outfile.close()




# Closing file
