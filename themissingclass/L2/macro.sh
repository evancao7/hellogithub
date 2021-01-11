#!/bin/bash
marco(){
        foo=$(pwd)
        export MARCO=$foo
}
polo(){
        cd "$MARCO" || echo "cd error"
}
