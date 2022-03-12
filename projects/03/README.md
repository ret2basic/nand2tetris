# Project 3

In this project, we are going to implement **RAM** and **Program Counter** based on the combinatorial gates from Project 1 and 2. 

**Note:** in HDL, bits are numbered from right to left, starting with 0. For example, we have address = abcdef, then:

- `address[0] = f`
- `address[1] = e`
- `address[2] = d`
- `address[3] = c`
- `address[4] = b`
- `address[5] = a`

## 1. Bit

We use `Mux` to select `out[t+1] = in[t]` or `out[t+1] = out[t]` based on the value of `load`, then use `DFF` to "shift" the output to the next clock cycle. Note that this chip is a loop: the output of `Mux` is the input of `DFF`, and the output of `DFF` is the input of `Mux`.

## 2. Register

Apply `Bit` to each bit of `in[16]`.

## 3. RAM8

1. Use `DMux8Way` to assign `load` for each register.
2. Use `Register` on each register.
3. Use `Mux8Way16` to select the correct register based on the given address. If `load==1`, then the value of this register is set to the value of `in[16]`.

## 4. RAM64

Note that `RAM64 = RAM8 * 8`. Here `address[0..2]` is for selecting one of the `RAM8` chips, and `address[3..5]` is for selecting one of the registers within the selected `RAM8`.

## 5. RAM512

Note that `RAM512 = RAM64 * 8`. Here `address[0..5]` is for selecting one of the `RAM64` chips, and `address[6..8]` is for selecting one of the registers within the selected `RAM64`.

## 6. RAM4K

Note that `RAM4K = RAM512 * 8`. Here `address[0..8]` is for selecting one of the `RAM512` chips, and `address[9..11]` is for selecting one of the registers within the selected `RAM512`.

## 7. RAM16K

Note that `RAM16K = RAM4K * 4`, so we use `DMux4Way` and `Mux4Way16` for this chip. Here `address[0..11]` is for selecting one of the `RAM4K` chips, and `address[12..13]` is for selecting one of the registers within the selected `RAM4K`.

## 8. PC

