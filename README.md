# somafm
Bash scripts to download all somafm playlists

## Invocation

Make sure the scripts are in your `bash` `${PATH}` variable and run

```bash
somafm_download_playlists.sh
```

in order to download all the `.pls`' into the current working directory.

To concatenate into a single `.m3u` that can easily be loaded into [Rhythmbox][rhythmbox] or [MOC][moc], just run

```bash
somafm_pls2m3u.py -new *.pls > all.m3u
```

and open `all.m3u` in [Rhythmbox][rhythmbox] or save it as the [MOC][moc] playlist. You can also omit the `-new` in order to append to a [MOC][moc] playlist.



[rhythmbox]: https://en.wikipedia.org/wiki/Rhythmbox
[moc]: https://en.wikipedia.org/wiki/Music_on_Console
