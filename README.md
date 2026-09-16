# pythermiagenesis

A Python library for Thermia Diplomat Inverter, Mega, and Calibra RXT heat pumps. The Calibra RXT profile also supports the equivalent Stiebel-Eltron WPE-I 07.1.

This library communicates with the device using Modbus TCP.
Set BMC to Modbus TCP on your heat pump to enable communication through this library.

## documentation

Thermia Modbus TCP documentation: 
- V10:  <https://www.tcmadmin.thermia.se/docroot/dokumentbank/Modbus%20protocol%20for%20Genesis%20platform%2010.pdf>
- V17.1:  <https://www.geotherma.be/wp-content/uploads/2026/02/Modbus-protocol-for-Genesis-platform-17.1-MEGA.pdf>

## notes

1. Be aware that some registers such for example "Compressor operating hours" will require a 32 bit read from two registers if the value is larger than 65535. This library does not handle this automatically, you will have to do this manually. This is explained in the manufacturer documentation.

## Models

- `mega`: Thermia Mega
- `inverter`: Thermia Diplomat Inverter
- `calibra_rxt`: Thermia Calibra RXT
- `stiebel_wpe_i_07_1`: Stiebel-Eltron WPE-I 07.1

Legacy `mega` and `inverter` identifiers remain unchanged.

```python
thermia = ThermiaGenesis("192.168.1.111", kind="calibra_rxt")
await thermia.async_update()
```
