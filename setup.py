from setuptools import setup, find_packages

setup(
    name='my-python-lib',                      # 项目名称
    version='0.1',                             # 版本
    author='Your Name',                        # 作者
    author_email='your.email@example.com',     # 作者邮箱
    description='A brief description of my-python-lib.',
    long_description=open('README.md').read(),  # 详细描述
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my-python-lib',  # 项目链接
    packages=find_packages(where='src'),       # 查找包
    package_dir={'': 'src'},                   # 指定包根目录
    install_requires=[                         # 依赖
        # 在这里列出你需要的库，如:
        'requests>=2.24.0',
        'numpy',
    ],
    classifiers=[                              # 元数据
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',                  # Python 版本要求
)