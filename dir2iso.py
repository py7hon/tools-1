import subprocess
import shlex
import argparse
import sys
def command(argv=None):
    "untuk melakukan perintah cli "
    parse=argparse.ArgumentParser(description="dir2iso is a simple CLI program for convert or make iso image from directory using genisoimage")
    parse.add_argument("-f","--folder",help="name folder")
    parse.add_argument("-l","--label",help="label for iso image")
    parse.add_argument("-o","--output", help="name file for iso file")
    
    result=parse.parse_args(argv)
    return(result.folder,result.label,result.output)

def convert(label,hasil,folder):
    # genisoimage -f -J -joliet-long -r -allow-lowercase -allow-multidot -iso-level 3 -volid "directory" -sysid LINUX -volset-size 1 -volset-seqno 1 -o "result.iso" "directory"'
    "fungsi untuk membuat file iso dari folder"
    query='genisoimage -f -J -joliet-long -r -allow-lowercase -allow-multidot -iso-level 3 -volid "{0}" -sysid LINUX -volset-size 1 -volset-seqno 1 -no-cache-inodes -full-iso9660-filenames -o "{1}" "{2}"'.format(label,hasil,folder)
    cmd = shlex.split(shlex.quote(query))
    execution = subprocess.Popen(cmd, shell=True).communicate()
    return execution

if __name__ == "__main__":
    folder,label,hasil=command(sys.argv[1:])
    # print(command(sys.argv[1:]))    
    convert(label=label,hasil=hasil,folder=folder)

