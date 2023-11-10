def mining_algorithm():
    b = 1  # block number
    rho = 1  # round

    runner_up = False

    while True:
        if rho == 1:
            nonce = find_block_nonce(b)
            if nonce:
                # nonce found
                append_new_block(b)
                announce_block(b)
                b += 1
                rho = 2  # Enter power-save mode
            else:
                if valid_block_received(b):
                    append_new_block(b)
                    b += 1
                    rho = 2
                    continue_find_block_nonce(b)
                    if nonce:
                        runner_up = True
                        announce_runner_up_block(b)
                    else:
                        if runner_up_block_received(b):
                            abort_mining(b)  # Enter power-save mode
        else:
            # second round: rho = 2
            if runner_up:
                nonce = find_block_nonce(b)
                if nonce:
                    append_new_block(b)
                    announce_block(b)
                else:
                    if valid_block_received(b):
                        append_new_block(b)
                        abort_mining(b)
                b += 1
                rho = 1
                runner_up = False
            else:
                # not a runner-up
                if valid_block_received(b):
                    append_new_block(b)
                    b += 1
                    rho = 1  # Exit power-save mode
