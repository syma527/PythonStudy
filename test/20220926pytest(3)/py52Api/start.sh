echo "开始创建python镜像执行python自动化测试"
#docker build -t py5220220914 .

docker run --rm -w=$WORKSPACE --volumes-from=pyjenkins pythondemo:haili

#docker rmi py5220220914
echo "python自动化测试执行完成"