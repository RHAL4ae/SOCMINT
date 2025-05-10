class User {
  final String? name;
  final String? emiratesId;

  User({this.name, this.emiratesId});

  factory User.fromJson(Map<String, dynamic> json) {
    return User(
      name: json['name'],
      emiratesId: json['emirates_id'],
    );
  }
}
