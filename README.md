Proof-of-concept code for backrunning private transaction using MPC. This repository contains the code and instructions on how to run it. Please find the background information on https://writings.flashbots.net/.

* Clone MP-SPDZ repository:
```
git clone https://github.com/data61/MP-SPDZ.git
```

* Add support for secret integer size of 256 bit (instead of just 64 bit) and integer division as well as square root on 256 bit integers:
```
cd MP-SPDZ
echo "MOD = -DGFP_MOD_SZ=17" > CONFIG.mine
```

* Compile and setup MP-SPDZ:
```
make -j tldr
make -j semi-party.x
make -j replicated-field-party.x
./Scripts/setup-ssl.sh 3
cd ..
```

* Copy proof-of-concept code and searcher input to source directory:
```
cp -ap backrun.mpc MP-SPDZ/Programs/Source/
cp -ap Input-P1-0 MP-SPDZ/Player-Data/
```


* Convert raw user transaction to input format expected by the MPC program (and put it into the right directory).
```
./tx2bytes.py 0xf90152038502cb4178008302dd09947a250d5630b4cf539739df2c5dacb4c659f2488d88340aad21b3b70000b8e47ff36ab5000000000000000000000000000000000000000000000000000000011bc8ba630000000000000000000000000000000000000000000000000000000000000080000000000000000000000000b3d8374bda9b975beefde96498fd371b484bdc0d00000000000000000000000000000000000000000000000000000000638850650000000000000000000000000000000000000000000000000000000000000002000000000000000000000000c02aaa39b223fe8d0a0e5c4f27ead9083c756cc2000000000000000000000000dac17f958d2ee523a2206206994597c13d831ec701a0cdd4cadbcf7bd4720519d70f9ab34069f108a3a8fe87e73933a6b4a9fd14f083a0483a7c77b0d24b4abd76713f888cf918a79685fb0fb0349bd90868513b4210e3 > MP-SPDZ/Player-Data/Input-P0-0
```

* Compile the PoC code:
```
cd MP-SPDZ
./compile.py -M backrun
```

* Execute program (in a weak security model to speedup execution. Note that execution still takes several minutes in that model):
```
./Scripts/rep-field.sh backrun
```

* Convert MPC program output to raw transaction.
```
cd ..
./bytes2tx.py "[249, 1, 139, 101, 133, 2, 203, 65, 120, 0, 131, 2, 221, 140, 148, 122, 37, 13, 86, 48, 180, 207, 83, 151, 57, 223, 44, 93, 172, 180, 198, 89, 242, 72, 141, 0, 185, 1, 36, 24, 203, 175, 229, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 84, 52, 4, 200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 70, 176, 59, 14, 175, 96, 167, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 160, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 78, 237, 143, 122, 29, 241, 154, 127, 183, 204, 153, 177, 137, 9, 217, 157, 6, 85, 68, 178, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 99, 136, 80, 109, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 218, 193, 127, 149, 141, 46, 229, 35, 162, 32, 98, 6, 153, 69, 151, 193, 61, 131, 30, 199, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 192, 42, 170, 57, 178, 35, 254, 141, 10, 14, 92, 79, 39, 234, 217, 8, 60, 117, 108, 194, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 160, 205, 212, 202, 219, 207, 123, 212, 114, 5, 25, 215, 15, 154, 179, 64, 105, 241, 8, 163, 168, 254, 135, 231, 57, 51, 166, 180, 169, 253, 20, 240, 131, 160, 72, 58, 124, 119, 176, 210, 75, 74, 189, 118, 113, 63, 136, 140, 249, 24, 167, 150, 133, 251, 15, 176, 52, 155, 217, 8, 104, 81, 59, 66, 16, 227, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]"
```

* Use https://flightwallet.github.io/decode-eth-tx/ for example to decode the raw backrunning transaction:
0xf9016c81808502cb4178008302dd8c947a250d5630b4cf539739df2c5dacb4c659f2488d80b9010418cbafe500000000000000000000000000000000000000000000000000000000543f12550000000000000000000000000000000000000000000000000f48b18507636ba400000000000000000000000000000000000000000000000000000000000000a00000000000000000000000004eed8f7a1df19a7fb7cc99b18909d99d065544b2000000000000000000000000000000000000000000000000000000006388506d0000000000000000000000000000000000000000000000000000000000000002000000000000000000000000dac17f958d2ee523a2206206994597c13d831ec7000000000000000000000000c02aaa39b223fe8d0a0e5c4f27ead9083c756cc227a0cdd4cadbcf7bd4720519d70f9ab34069f108a3a8fe87e73933a6b4a9fd14f083a0483a7c77b0d24b4abd76713f888cf918a79685fb0fb0349bd90868513b4210e3
