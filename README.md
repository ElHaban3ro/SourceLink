
#  SourceLink
[![License: MIT](https://img.shields.io/badge/License-MIT-yellowgreen.svg?style=flat-square)](https://opensource.org/licenses/MIT) [![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg?style=flat-square&logo=python)](https://www.python.org/downloads/release/python-310/) [![PyPi Package](https://img.shields.io/badge/PyPi_Package-pip_install_MovieTool-yellow.svg?style=flat-square&logo=pypi)](https://pypi.org/project/SourceLink/) [![GitGub Repositorie](https://img.shields.io/badge/GitHub_Repositorie-MovieTool-gray.svg?style=flat-square&logo=github)](https://github.com/ElHaban3ro/SourceLink/)


Generates through playlists a txt file with the acknowledgements or resources used for an audio visual content. I made this little tool because I made a video on my youtube channel and all the resources I was using I was putting them in a playlist within the same Youtube. To extract each link from each video would take me too long and it was boring, so I created this tool (which in the end took me longer than it would have taken me to do it manually, but you have to think about the future).

  
## Use
At the moment the script works only from script, but in the future (when I need it again) I will add the option to do it via console (which is a bit faster for the case).

***To start, install SourceLink:***
```bash
pip install SourceLink
```
***Start to using:***
```python
from SourceLink.Contributors import ContributorsGen


genList = ContributorsGen('SAVE_ROUTE')
genList.contributror_file(['PLAYLIST_LIST',  'https://www.youtube.com/playlist?list=PLozfyPKLTR99Frrt3Jnju6Ag9SyDpeCoK'])
```
***This generates the following:***
*(in txt file)*
```
Thanks to:

- https://www.youtube.com/watch?v=qNaz3sYYnWs
- https://www.youtube.com/watch?v=XjmIlOS-CjM
- https://www.youtube.com/watch?v=aR-KAldshAE
- https://www.youtube.com/watch?v=JB_NLzN3anI
```



---

[![Contact Twitter](https://img.shields.io/badge/Twitter-ElHaban3ro-9cf.svg?style=for-the-badge&logo=twitter)](https://twitter.com/ElHaban3ro)
[![Contact Discord](https://img.shields.io/badge/Discord-JOIN_TO_MY_DISCORD_SERVER-lightblue?style=for-the-badge&logo=discord)](https://discord.gg/NGp9YbYJ8F)
[![Contact Discord](https://img.shields.io/badge/GitHub-ElHaban3ro-lightgray?style=for-the-badge&logo=github)](https://github.com/ElHaban3ro)