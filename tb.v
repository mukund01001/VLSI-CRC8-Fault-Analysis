module tb;
    reg [7:0] data_in;
    reg [7:0] crc_in;
    wire [7:0] crc_out;
    
    crc8 uut (
        .data_in(data_in),
        .crc_in(crc_in),
        .crc_out(crc_out)
    );
    
    initial begin
        $dumpfile("wave.vcd");
        $dumpvars(0, tb);
        
        // Test Vector 1
        data_in = 8'hA5; crc_in = 8'h00; #10;
        // Test Vector 2
        data_in = 8'hFF; crc_in = crc_out; #10;
        // Test Vector 3
        data_in = 8'h5A; crc_in = crc_out; #10;
        
        $finish;
    end
endmodule
