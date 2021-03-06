# !!CHANGE THIS!!
HVERSION=2.7.6

#!! AND LET IT RUN
#brew install gcc autoconf automake libtool cmake snappy gzip bzip2 zlib openssl

cd ~
mkdir -p tmp
cd ~/tmp

wget https://github.com/google/protobuf/releases/download/v2.5.0/protobuf-2.5.0.tar.gz
tar -xzf protobuf-2.5.0.tar.gz
cd protobuf-2.5.0
./configure
make
make check
make install
protoc --version

cd /usr/local/include
ln -s ../opt/openssl/include/openssl .

cd ~/tmp
git clone https://github.com/apache/hadoop.git
cd hadoop
git checkout branch-$HVERSION
mvn package -Pdist,native -DskipTests -Dtar

cp -R hadoop-dist/target/hadoop-$HVERSION/lib $HADOOP_HOME

export HADOOP_OPTS="-Djava.library.path=${HADOOP_HOME}/lib/native"
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${HADOOP_HOME}/lib/native
export JAVA_LIBRARY_PATH=$JAVA_LIBRARY_PATH:${HADOOP_HOME}/lib/native

hadoop checknative -a

