#!/usr/bin/python3

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys
import atheris
with atheris.instrument_imports():
  import yaml.reader

@atheris.instrument_func
def TestOneInput(data):
    if len(data) < 1:
        return 
    try:
        stream = yaml.reader.Reader(data)
        while stream.peek() != u'\0':
            stream.forward()
    except yaml.reader.ReaderError:
        None
    except RecursionError:
        pass

    return 

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
