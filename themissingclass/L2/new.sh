#!/bin/bash
fd . -0 -t f | xargs -0 stat -f '%m%t%Sm %N' | sort -n | cut -f2- | tail -n 1
